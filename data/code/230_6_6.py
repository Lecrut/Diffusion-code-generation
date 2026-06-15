class ObjectProcessor:
    def __init__(self):
        self.data = [
            {"id": 1, "name": "Apple", "type": "Fruit"},
            {"id": 2, "name": "Carrot", "type": "Vegetable"},
            {"id": 3, "name": "Banana", "type": "Fruit"}
        ]
    def print_object_details(self):
        for obj in self.data:
            print(f"Object ID: {obj['id']}, Name: {obj['name']}, Type: {obj['type']}")
if __name__ == '__main__':
    processor = ObjectProcessor()
    processor.print_object_details()