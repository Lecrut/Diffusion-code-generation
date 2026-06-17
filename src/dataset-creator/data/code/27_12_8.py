from collections import defaultdict
class FruitProcessor:
    def group_by_type(self, fruits):
        grouped = {}
        for fruit in map(lambda x: (x['name'], x.get('type', 'unknown')), fruits):
            name, f_type = fruit[0], fruit[1]
            if f_type not in grouped:
                grouped[f_type] = []
            grouped[f_type].append(name)
        return dict(grouped)
if __name__ == '__main__':
    sample_data = [
        {'name': 'Apple', 'type': 'Pome'},
        {'name': 'Banana', 'type': 'Berry'},
        {'name': 'Orange', 'type': 'Pome'},
        {'name': 'Grape', 'type': 'Berry'},
        {'name': 'Mango', 'type': 'Drupe'}
    ]
    processor = FruitProcessor()
    result = processor.group_by_type(sample_data)
    for f_type, names in sorted(result.items()):
        print(f"{f_type}: {names}")