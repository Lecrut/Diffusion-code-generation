class FruitProcessor:
    def group_by_type(self, fruits):
        grouped = {}
        for fruit in map(lambda f: (f['name'], f.get('type')), fruits):
            name, type_ = fruit
            if not isinstance(type_, str) or type_.strip() == '':
                continue
            if type_ not in grouped:
                grouped[type_] = []
            grouped[type_].append(name)
        return grouped
if __name__ == '__main__':
    sample_data = [
        {'name': 'Apple', 'type': 'Pome'},
        {'name': 'Banana', 'type': 'Berry'},
        {'name': 'Orange', 'type': ''},
        {'name': 'Grape', 'type': 'Berry'},
        {'name': 'Mango', 'type': 'Drupe'}
    ]
    processor = FruitProcessor()
    result = processor.group_by_type(sample_data)
    print(result)