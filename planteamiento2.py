class Admin:
    def __init__(self, nombre="", apellido="", numero=0):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.contactos = []

    def crear(self):
     try:
        nombre = input("\nIngrese un nombre: ").lower()
        apellido = input("\nIngrese un apellido: ").lower()
        numero = int(input("\nIngrese el número de telefono: "))

        guardar = Admin(nombre, apellido, numero)

        self.contactos.append(guardar)

     except ValueError:
         print("\nError a los datos ingresados")
    
    def mostrar(self):
     try:
        for c in self.contactos:
            print("============================")
            print("->",c.nombre, "|", c.apellido, "|", c.numero)
            print("============================")
        if  not self.contactos:
            print("============================")
            print("\nNo se encuentra ningún contacto registrado...")
            print("============================")

     except ValueError:
         print("\nError a los datos ingresados")


class eliminar:
    def __init__(self, admin):
        self.admin = admin  

    def borrar(self):
     try:
        print("============================")
        nombreEliminar = input("\nIngresa el nombre que deseas borrar: ").lower()

        if nombreEliminar != self.admin.nombre:
            print("============================")
            print("\nEl nombre que ingresaste no se encuentra")
            print("============================")
        print("\nSi desea puedes eliminar con el número")
        print("============================")
        numeroEliminar = int(input("\nIngresa el número que desea eliminar o si no quiere ingresa 0: "))
        for c in self.admin.contactos:
            if c.nombre == nombreEliminar:
                self.admin.contactos.remove(c)
                print("============================")
                print("\nEl contacto se ha eliminado en tu registro: ->", c.nombre)
                print("============================")
                return
            elif c.numero == numeroEliminar:
                self.admin.contactos.remove(c)
                print("============================")
                print("El contacto se ha eliminado en tu registro : ->",c.nombre)
                print("============================")
                return
            
     except ValueError:
         print("============================")
         print("\nError a los datos ingresados")
         print("============================")
        
            
administrar = Admin()



while True:
    print("\nMenú de registro")
    print("\n1. Crear Contacto")
    print("\n2. Mostrar Conctacto")
    print("\n3. Eliminar Conctato")
  
    opcion= int(input("\nIngrese un número del 1 al 4: "))

    if opcion == 1:
        print("\nCrear Contacto")
        administrar.crear()

    elif opcion == 2:
        print("\nMostrar Conctacto")
        administrar.mostrar()

    elif opcion == 3:
        print("\nEliminar Contacto")
        delete = eliminar(administrar)
        delete.borrar()
    elif opcion == 4:
        print("\nGracias por tu visita")
        break

    elif opcion > 5 or opcion == 0:
        print("\nEsta opción no se encuentra")







