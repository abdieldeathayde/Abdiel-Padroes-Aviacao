class ComissarioBordo:
    def __init__(self, nome, id_comissario):
        self.nome = nome
        self.id_comissario = id_comissario

    def __repr__(self):
        return f"{self.nome} (ID: {self.id_comissario})"


class Comandante:
    def __init__(self, nome, id_comandante, anos_experiencia):
        self.nome = nome
        self.id_comandante = id_comandante
        self.anos_experiencia = anos_experiencia

    def __repr__(self):
        return f"{self.nome} (ID: {self.id_comandante}, Anos de Experiência: {self.anos_experiencia})"


class Voo:
    def __init__(self, numero_voo, companhia_aerea, origem, destino):
        self.numero_voo = numero_voo
        self.companhia_aerea = companhia_aerea
        self.origem = origem
        self.destino = destino
        self.comissarios = []
        self.comandantes = []

    def adicionar_comissario(self, comissario):
        self.comissarios.append(comissario)

    def adicionar_comandante(self, comandante):
        self.comandantes.append(comandante)

    def __repr__(self):
        return (f"Voo {self.numero_voo} - {self.companhia_aerea}:\n"
                f"Origem: {self.origem}\nDestino: {self.destino}\n"
                f"Comissários: {self.comissarios}\nComandantes: {self.comandantes}")


# Exemplo de uso
voo1 = Voo("AZ123", "Azul", "GRU", "JFK")
comissario1 = ComissarioBordo("Maria Silva", "CB101")
comandante1 = Comandante("Carlos Souza", "CMD202", 15)

voo1.adicionar_comissario(comissario1)
voo1.adicionar_comandante(comandante1)

print(voo1)


class ControleTrafegoAereo:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ControleTrafegoAereo, cls).__new__(cls)
        return cls._instancia

    def __init__(self):
        self.voos_monitorados = []

    def adicionar_voo(self, voo):
        self.voos_monitorados.append(voo)

# Uso do Singleton
controle1 = ControleTrafegoAereo()
controle2 = ControleTrafegoAereo()

print(controle1 is controle2)  # True, pois ambas são a mesma instância

class VooBuilder:
    def __init__(self):
        self.numero_voo = None
        self.companhia_aerea = None
        self.origem = None
        self.destino = None
        self.comissarios = []
        self.comandantes = []

    def set_numero_voo(self, numero_voo):
        self.numero_voo = numero_voo
        return self

    def set_companhia_aerea(self, companhia_aerea):
        self.companhia_aerea = companhia_aerea
        return self

    def set_origem(self, origem):
        self.origem = origem
        return self

    def set_destino(self, destino):
        self.destino = destino
        return self

    def adicionar_comissario(self, comissario):
        self.comissarios.append(comissario)
        return self

    def adicionar_comandante(self, comandante):
        self.comandantes.append(comandante)
        return self

    def build(self):
        voo = Voo(self.numero_voo, self.companhia_aerea, self.origem, self.destino)
        voo.comissarios = self.comissarios
        voo.comandantes = self.comandantes
        return voo

# Uso do Builder
builder = VooBuilder()
voo = (builder.set_numero_voo("AZ123")
             .set_companhia_aerea("Azul")
             .set_origem("GRU")
             .set_destino("JFK")
             .adicionar_comissario(ComissarioBordo("Maria Silva", "CB101"))
             .adicionar_comandante(Comandante("Carlos Souza", "CMD202", 15))
             .build())

print(voo)

class SistemaExterno:
    def __init__(self):
        self.lista_voos = []

    def adicionar_voo_externo(self, voo_str):
        self.lista_voos.append(voo_str)

class AdapterVoo:
    def __init__(self, voo):
        self.voo = voo

    def converter_para_externo(self):
        return f"{self.voo.numero_voo} - {self.voo.companhia_aerea} ({self.voo.origem} -> {self.voo.destino})"

# Uso do Adapter
voo_adapter = AdapterVoo(voo)
sistema_externo = SistemaExterno()
sistema_externo.adicionar_voo_externo(voo_adapter.converter_para_externo())

print(sistema_externo.lista_voos)

class ObservadorVoo:
    def atualizar(self, voo):
        raise NotImplementedError

class Passageiro(ObservadorVoo):
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, voo):
        print(f"Passageiro {self.nome} notificado: Voo {voo.numero_voo} atualizado!")

class VooObservable:
    def __init__(self, numero_voo):
        self.numero_voo = numero_voo
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self.observadores:
            observador.atualizar(self)

    def alterar_voo(self, nova_origem, novo_destino):
        self.origem = nova_origem
        self.destino = novo_destino
        self.notificar_observadores()

# Uso do Observer
voo_observable = VooObservable("AZ123")
passageiro1 = Passageiro("João")

voo_observable.adicionar_observador(passageiro1)
voo_observable.alterar_voo("GRU", "LAX")  # Notifica os observadores sobre a mudança
