class FruitProcessor:
    def group_by_type(self, fruits):
        grouped = {}
        for fruit in map(lambda x: (x['name'], x['type']), fruits):
            name, f_type = fruit
            if f_type not in grouped:
                grouped[f_type] = []
            grouped[f_type].append(name)
        return grouped
if __name__ == '__main__':
    sample_fruits = [
        {'name': 'Apple', 'type': 'Rosaceae'},
        {'name': 'Banana', 'type': 'Musaceae'},
        {'name': 'Orange', 'type': 'Rutaceae'},
        {'name': 'Grape', 'type': 'Vitaceae'},
    ]
    processor = FruitProcessor()
    result = processor.group_by_type(sample_fruits)
    for fruit_type, names in sorted(result.items()):
        print(f"{fruit_type}: {names}")