class ObjectPrinter:
    def __init__(self):
        self.data_set = [
            {"id": 1, "name": "Apple", "color": "Red"},
            {"id": 2, "name": "Banana", "color": "Yellow"},
            {"id": 3, "name": "Grape", "color": "Purple"}
        ]
    def print_all_objects(self):
        for obj in self.data_set:
            print(f"Object found: ID {obj['id']}, Name {obj['name']}, Color {obj['color']}")
if __name__ == '__main__':
    printer = ObjectPrinter()
    printer.print_all_objects()