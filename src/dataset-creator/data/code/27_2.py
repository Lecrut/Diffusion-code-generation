from collections import defaultdict
def categorize_fruit(fruits: list[dict]) -> dict[str, list[dict]]:
    categorized = defaultdict(list)
    for fruit in fruits:
        if 'citrus' in str(fruit.get('type', '')).lower():
            categorized['citrus'].append(fruit)
        elif 'berry' in str(fruit.get('type', '')).lower() or 'blueberry' in str(fruit.get('type', '')).lower():
            categorized['berry'].append(fruit)
        else:
            stone_types = ['peach', 'plum', 'apricot']
            if any(stone_type in str(fruit.get('type', '')) for stone_type in stone_types):
                categorized['stone_fruit'].append(fruit)
    return dict(categorized)
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Orange', 'type': 'citrus'},
        {'id': 2, 'name': 'Apple', 'type': 'fruit'},
        {'id': 3, 'name': 'Strawberry', 'type': 'berry'},
        {'id': 4, 'name': 'Peach', 'type': 'stone_fruit'},
        {'id': 5, 'name': 'Blueberry', 'type': 'fruit'}
    ]
    result = categorize_fruit(sample_data)
    for group_name in ['citrus', 'berry', 'stone_fruit']:
        if group_name in result:
            print(f"{group_name}: {result[group_name]}")