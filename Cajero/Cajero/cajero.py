
# Declaramos el cajero como Class
class Cajero:
    def __init__(self):
        self.continuar = True
        self.cuenta = 0
        self.menu()

    def menu(self):
    # Creamos un menú de selección
        opcion = 0
        while opcion != 5:
            print(".::Bienvenido al Cajero Automatico del banco Los Tres Patitos::.")
            print("\t\t   ✬✬Menú✬✬")
            print("1- Depositar")
            print("2- Retirar")
            print("3- Consultar cuenta")
            print("4- Salir")

        # Los self que coloqué es para que al seleccionar una opción
        # esta nos lleve al sitio correspondiente.
            opcion = input("Su opción es ")
            if self.continuar:
                if opcion == "1":
                    self.deposito()
                elif opcion == "2":
                    self.retiro()
                elif opcion == "3":
                    self.ver()
                elif opcion == "4":
                    print(".::Gracias por usar nuestros servicios. Vuelva pronto::.")
                    break
                else:
                    print("El número que digitó no está en las opciones, por favor, dígite de nuevo")

        print()

    def deposito(self):
        print(".::¿Cuánto desea depositar?::.")
        print("1. 2000₡")
        print("2. 5000₡")
        print("3. 10.000₡")
        print("4. Otro monto")
        print("5. Regresar a la sección anterior")
    # Aquí repetimos el mismo procedimiento en cuestión
        depositar = input("Digite el número asignado: ")
        if self.continuar:

            if depositar == "1":
                deposito1 = 2000
                input(f"Ha depositado {deposito1}₡ en su cuenta")
                self.deposito()
                self.cuenta += deposito1

            elif depositar == "2":
                deposito2 = 5000
                input(f"Ha depositado {deposito2}₡ en su cuenta")
                self.cuenta += deposito2
                self.deposito()

            elif depositar == "3":

                deposito3 = 10000
                input(f"Ha depositado {deposito3}₡ en su cuenta")
                self.cuenta += deposito3
                self.menu()

            elif depositar == "4":
                deposito4 = int(input("Dígite el monto a depositar: "))
                print(f"Ha depositado {deposito4}₡ en su cuenta")
                self.cuenta += deposito4
                self.deposito()

            elif depositar == "5":
                print("Regresando a la sección anterior")
                self.menu()

    def retiro(self):
        print(".::¿Cuánto desea retirar?::.")
        print("1. 2000₡")
        print("2. 5000₡")
        print("3. 10000₡")
        print("4. Otro monto")
        print("5. Regresar a la sección anterior")

        retirar = input("Digite el número asignado: ")
    # En la sección de acá, le indicamos al código que almacene
    # y sume o reste los valores que se depositan
        if retirar == "1":
            retiro1 = 2000
            input(f"Ha retirado {retiro1}₡ en su cuenta")
            self.retiro()
            self.cuenta -= retiro1

        elif retirar == "2":
            retiro2 = 5000
            input(f"Ha retirado {retiro2}₡ en su cuenta")
            self.retiro()
            self.cuenta -= retiro2

        elif retirar == "3":
            retiro3 = 10000
            input(f"Ha retirado {retiro3}₡ en su cuenta")
            self.retiro()
            self.cuenta -= retiro3

        elif retirar == "4":
            retiro4 = int(input("Dígite el monto a retirar: "))
            print(f"Ha depositado {retiro4}₡ en su cuenta")
            self.cuenta -= retiro4
            self.deposito()

        elif retirar == "5":
            print("Regresando a la sección anterior")
            self.menu()

# El self muestra todos los valores vinculados anteriormente
    def ver(self):
        print(f"Su saldo es de: {self.cuenta}₡")


app = Cajero()