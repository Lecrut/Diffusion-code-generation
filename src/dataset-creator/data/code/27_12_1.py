class FruitProcessor:
    def group_by_type(self, fruits):
        grouped = {}
        for fruit in map(lambda f: (f['name'], f.get('type', 'unknown')), fruits):
            name, type_ = fruit
            if not isinstance(type_, str) or len(type_) == 0:
                type_ = 'other'
            if name not in grouped:
                grouped[name] = {'count': 1, 'types': {}}
            else:
                grouped[name]['count'] += 1
        return list(grouped.values())
if __name__ == '__main__':
    sample_fruits = [
        {'name': 'Apple', 'type': 'Pome'},
        {'name': 'Banana', 'type': 'Berry'},
        {'name': 'Orange', 'type': 'Pome'},
        {'name': 'Grape', 'type': 'Berry'},
    ]
    processor = FruitProcessor()
    result = processor.group_by_type(sample_fruits)
    print(result)