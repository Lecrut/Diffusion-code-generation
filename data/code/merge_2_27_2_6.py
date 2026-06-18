from collections import defaultdict
def categorize_fruit(fruits: list[dict[str, str]]) -> dict[str, list[str]]:
    categorized = defaultdict(list)
    for fruit in fruits:
        name = fruit.get('name', '').lower()
        if 'orange' in name or 'lemon' in name or 'lime' in name or 'grapefruit' in name:
            categorized['citrus'].append(fruit['name'])
        elif 'strawberry' in name or 'blueberry' in name or 'raspberry' in name or 'blackberry' in name:
            categorized['berry'].append(fruit['name'])
        else:
            if 'apple' in name or 'peach' in name or 'plum' in name or 'cherry' in name:
                categorized['stone_fruit'].append(fruit['name'])
    return dict(categorized)
if __name__ == '__main__':
    sample_data = [
        {'name': 'Orange'},
        {'name': 'Lemon'},
        {'name': 'Strawberry'},
        {'name': 'Blueberry'},
        {'name': 'Peach'},
        {'name': 'Grapefruit'}
    ]
    result = categorize_fruit(sample_data)
    print(result)