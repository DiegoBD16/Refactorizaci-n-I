# Sistema de venta de billetes de avión

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha, salida, llegada, precio):
        self.numero_vuelo = numero_vuelo
        self.origen_del_vuelo = origen
        self.destino_del_vuelo = destino
        self.fecha_del_vuelo = fecha
        self.fecha_de_salida = salida
        self.fecha_de_llegada = llegada
        self.precio_del_vuelo = precio

    def __str__(self):
        return(f"Número de vuelo: {self.numero_vuelo}, Origen: {self.origen_del_vuelo}, Destino: {self.destino_del_vuelo}, Fecha: {self.fecha_del_vuelo}, Hora de salida: {self.fecha_de_salida}, Hora de llegada: {self.fecha_de_llegada}, Precio: {self.precio_del_vuelo}")

class Pasajero:
    def __init__(self, nombre, apellido, edad, telefono, correo):
        self.nombre_del_pasajero = nombre
        self.apellido_del_pasajero = apellido
        self.edad_del_pasajero = edad
        self.telefono_del_pasajero = telefono
        self.correo_del_pasajero = correo

class Informacion:
    def __init__(self, vuelo, pasajero, asientos):
        self.vuelo = vuelo
        self.pasajero = pasajero
        self.asientos = asientos

def mostrar_vuelos_disponibles(vuelos):
    print("Vuelos disponibles:")
    for vuelo in vuelos:
        print(vuelo)

def reservar_asientos(cantidad):
    if cantidad <= 0:
            print("La cantidad de asientos debe ser mayor que cero.")
            return
    elif cantidad > 10:
        print("Lo sentimos, no se pueden reservar más de 10 asientos por reserva.")
        return
    elif cantidad > 0 and cantidad <= 10:
        return cantidad

def reservar_vuelo(lista, numero_vuelo, pasajero, cantidad_de_asientos):
    
    for v in lista:
        if v.numero_vuelo == numero_vuelo:
            reserva = Informacion(v, pasajero, cantidad_de_asientos)
            print(f"¡Reserva exitosa para el vuelo {v.numero_vuelo}!")
            print(f"Nombre del pasajero: {pasajero.nombre_del_pasajero} {pasajero.apellido_del_pasajero}, Asientos reservados: {reservar_asientos(cantidad_de_asientos)}")
            return
    print("No se encontró ningún vuelo con el número especificado.")


def main():
    vuelos = [
        Vuelo("AA123", "Nueva York", "Los Angeles", "2024-05-15", "08:00", "11:00", 250.00),
        Vuelo("AA456", "Los Angeles", "Chicago", "2024-05-20", "10:00", "13:00", 200.00),
        Vuelo("AA789", "Chicago", "Miami", "2024-05-25", "12:00", "15:00", 300.00)
    ]

    print("Bienvenido al sistema de venta de billetes de avión.")
    opcion = 0 #hago que opcion sea int
    while opcion != 3:
        opcion = int(input("Seleccione una opción:\n1. Ver vuelos disponibles\n2. Reservar vuelo\n3. finalizar \nIngrese su opción: "))
        if opcion == 1:
            mostrar_vuelos_disponibles(vuelos)
        elif opcion == 2:
            #extraer método
            nombre_pasajero = input("Ingrese su nombre: ")
            apellido_pasajero = input("Ingrese su apellido: ")
            edad_pasajero = int(input("Ingrese su edad: "))
            telefono_pasajero = input("Ingrese su número de teléfono: ")
            correo_pasajero = input("Ingrese su correo electrónico: ")

            pasajero = Pasajero(nombre_pasajero, apellido_pasajero, edad_pasajero, telefono_pasajero, correo_pasajero)

            #extraer método
            numero_del_vuelo = input("Ingrese el número de vuelo que desea reservar: ")
            cantidad_de_asientos = int(input("Ingrese la cantidad de asientos que desea reservar (máximo 10): "))

            reservar_vuelo(vuelos, numero_del_vuelo, pasajero, cantidad_de_asientos)
        else:
            print("Adios.")

if __name__ == "__main__":
    main()