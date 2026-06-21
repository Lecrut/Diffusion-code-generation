from typing import List, Dict

def initialize_items() -> List[Dict[str, str]]:
    items = [
        {'id': '001', 'name': 'Apple', 'category': 'Fruit'},
        {'id': '002', 'name': 'Banana', 'category': 'Fruit'},
        {'id': '003', 'name': 'Carrot', 'category': 'Vegetable'}
    ]
    return items

if __name__ == '__main__':
    sample_items = initialize_items()
    print(sample_items)