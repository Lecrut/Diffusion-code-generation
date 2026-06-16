from collections import defaultdict
from typing import Dict, List
def categorize_fruits(fruit_data: List[Dict[str, str]]) -> Dict[str, List[int]]:
    categorized = defaultdict(list)
    for fruit in fruit_data:
        if 'citrus' in fruit.get('type', '').lower():
            categorized['citrus'].append(fruit['id'])
        elif 'berry' in fruit.get('type', '').lower():
            categorized['berry'].append(fruit['id'])
        else:
            categorized['stone_fruit'].append(fruit['id'])
    return dict(categorized)
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'type': 'citrus'},
        {'id': 2, 'type': 'berry'},
        {'id': 3, 'type': 'stone_fruit'},
        {'id': 4, 'type': 'citrus'}
    ]
    result = categorize_fruits(sample_data)
    print(result)