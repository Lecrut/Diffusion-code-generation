class FruitProcessor:
    def group_by_type(self, fruits):
        grouped = {}
        for fruit in map(lambda f: (f['name'], f.get('type', 'unknown')), fruits):
            name, type_ = fruit
            if type_ not in grouped:
                grouped[type_] = []
            grouped[type_].append(name)
        return grouped
if __name__ == '__main__':
    sample_fruits = [
        {'name': 'Apple', 'type': 'Berry'},
        {'name': 'Banana', 'type': 'Fruit'},
        {'name': 'Cherry', 'type': 'Berry'},
        {'name': 'Date', 'type': 'Fruit'},
    ]
    processor = FruitProcessor()
    result = processor.group_by_type(sample_fruits)
    print(result)