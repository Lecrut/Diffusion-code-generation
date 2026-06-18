from collections import defaultdict
def categorize_fruit(fruits: list[dict[str, str]]) -> dict[str, list[str]]:
    categorized = defaultdict(list)
    for fruit in fruits:
        if 'citrus' in fruit.get('category', '').lower() or 'orange' in fruit.get('name', '').lower():
            categorized['citrus'].append(fruit['name'])
        elif 'berry' in fruit.get('category', '').lower() or 'strawberry' in fruit.get('name', '').lower():
            categorized['berry'].append(fruit['name'])
        else:
            if 'stone_fruit' not in [cat.lower() for cat in ['citrus', 'berry']]:
                categorized['stone_fruit'].append(fruit['name'])
    return dict(categorized)
if __name__ == '__main__':
    sample_data = [
        {'name': 'Apple', 'category': 'fresh'},
        {'name': 'Orange', 'category': 'citrus'},
        {'name': 'Strawberry', 'category': 'fruit'},
        {'name': 'Banana', 'category': 'tropical'},
    ]
    result = categorize_fruit(sample_data)
    print(result)