from collections import defaultdict
def categorize_fruit(fruits: list[dict[str, str]]) -> dict[str, list[str]]:
    categorized = defaultdict(list)
    for fruit in fruits:
        name = fruit.get('name', '')
        if 'orange' in name.lower() or 'lemon' in name.lower():
            categorized['citrus'].append(name)
        elif 'strawberry' in name.lower() or 'blueberry' in name.lower():
            categorized['berry'].append(name)
        else:
            categorized['stone_fruit'].append(name)
    return dict(categorized)
if __name__ == '__main__':
    sample_data = [
        {'name': 'Orange'},
        {'name': 'Lemon'},
        {'name': 'Strawberry'},
        {'name': 'Blueberry'},
        {'name': 'Peach'}
    ]
    result = categorize_fruit(sample_data)
    print(result)