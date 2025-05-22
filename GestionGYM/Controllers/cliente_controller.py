class ClienteController:

    def crearCliente(self, datos_cliente: dict) -> bool:
        # Lógica para crear un cliente
        print(f"Creando cliente con datos: {datos_cliente}")
        return True

    def actualizarCliente(self, idCliente: int, datos_actualizados: dict) -> bool:
        # Lógica para actualizar datos de un cliente
        print(f"Actualizando cliente {idCliente} con datos: {datos_actualizados}")
        return True

    def eliminarCliente(self, idCliente: int) -> bool:
        # Lógica para eliminar un cliente
        print(f"Eliminando cliente con ID: {idCliente}")
        return True

    def obtener(self, idCliente: int = None):
        # Lógica para obtener un cliente o lista de clientes
        if idCliente:
            print(f"Obteniendo cliente con ID: {idCliente}")
            return {"id": idCliente, "nombre": "Cliente Ejemplo"}
        else:
            print("Obteniendo lista de todos los clientes")
            return [
                {"id": 1, "nombre": "Cliente 1"},
                {"id": 2, "nombre": "Cliente 2"}
            ]


