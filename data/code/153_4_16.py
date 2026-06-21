from typing import Any, List

def item_exists(item: Any, items: List[Any]) -> bool:
    return item in items

if __name__ == '__main__':
    sample_item = 'apple'
    sample_list = ['banana', 'apple', 'cherry']
    print(item_exists(sample_item, sample_list))