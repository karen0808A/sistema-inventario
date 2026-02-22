import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                return

            with open(self.archivo, "r") as f:
                for linea in f:
                    try:
                        id_p, nombre, cantidad, precio = linea.strip().split(",")
                        self.productos[id_p] = Producto(
                            id_p, nombre, int(cantidad), float(precio)
                        )
                    except ValueError:
                        print("Línea corrupta ignorada.")
        except PermissionError:
            print("Error de permisos al leer el archivo.")

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(str(producto) + "\n")
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("Error de permisos al escribir el archivo.")

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[id_producto] = Producto(
                id_producto, nombre, cantidad, precio
            )
            self.guardar_inventario()
            print("Producto agregado.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos.values():
                print(
                    f"ID: {p.id_producto}, Nombre: {p.nombre}, "
                    f"Cantidad: {p.cantidad}, Precio: {p.precio}"
                )


if __name__ == "__main__":
    inv = Inventario()
    inv.agregar_producto("001", "Laptop", 5, 1200.50)
    inv.mostrar_inventario()
