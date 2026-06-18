class FruitProcessor:
    def group_by_type(self, fruits):
        return {fruit['type']: [f for f in fruits if f['type'] == fruit['type']] for fruit in fruits}
if __name__ == '__main__':
    sample_fruits = [
        {'name': 'Apple', 'type': 'Rosaceae'},
        {'name': 'Banana', 'type': 'Musaceae'},
        {'name': 'Orange', 'type': 'Rutaceae'},
        {'name': 'Grape', 'type': 'Vitaceae'},
        {'name': 'Pear', 'type': 'Rosaceae'}
    ]
    processor = FruitProcessor()
    grouped_data = processor.group_by_type(sample_fruits)
    for type_name, fruit_list in grouped_data.items():
        print(f"{type_name}: {fruit_list}")