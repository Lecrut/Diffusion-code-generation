from collections import defaultdict
def categorize_fruit(fruits: list[dict[str, str]]) -> dict[str, list[str]]:
    categorized = defaultdict(list)
    for fruit in fruits:
        name = fruit.get('name', '')
        type_ = fruit.get('type', '').lower()
        if 'citrus' in type_:
            categorized['citrus'].append(name)
        elif 'berry' in type_:
            categorized['berry'].append(name)
        elif 'stone' in type_:
            categorized['stone_fruit'].append(name)
    return dict(categorized)
if __name__ == '__main__':
    sample_data = [
        {'name': 'Orange', 'type': 'citrus'},
        {'name': 'Apple', 'type': 'berry'},
        {'name': 'Strawberry', 'type': 'berry'},
        {'name': 'Peach', 'type': 'stone_fruit'},
        {'name': 'Grapefruit', 'type': 'citrus'}
    ]
    result = categorize_fruit(sample_data)
    print(result)