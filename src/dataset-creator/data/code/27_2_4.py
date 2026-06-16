from collections import defaultdict
def categorize_fruit(fruits: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    fruit_groups = defaultdict(list)
    for fruit in fruits:
        name = fruit.get('name', '').lower()
        if 'orange' in name or 'lemon' in name or 'lime' in name:
            fruit_groups['citrus'].append(fruit)
        elif 'strawberry' in name or 'blueberry' in name or 'raspberry' in name:
            fruit_groups['berry'].append(fruit)
        else:
            if any(x in name for x in ['peach', 'plum', 'apricot']):
                fruit_groups['stone_fruit'].append(fruit)
    return dict(fruit_groups)
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