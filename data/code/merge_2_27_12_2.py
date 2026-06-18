class FruitProcessor:
    def group_by_type(self, fruits):
        grouped = {}
        for fruit in map(lambda f: (f['name'], f.get('type', 'unknown')), fruits):
            name, type_ = fruit
            if not isinstance(type_, str) or len(type_) == 0:
                continue
            if type_ not in grouped:
                grouped[type_] = []
            grouped[type_].append(name)
        return grouped
if __name__ == '__main__':
    sample_fruits = [
        {'name': 'Apple', 'type': 'Berry'},
        {'name': 'Banana', 'type': 'Fruit'},
        {'name': 'Cherry', 'type': 'Berry'},
        {'name': 'Date', 'type': ''},
        {'name': 'Elderberry', 'type': 'Berry'}
    ]
    processor = FruitProcessor()
    result = processor.group_by_type(sample_fruits)
    print(result)