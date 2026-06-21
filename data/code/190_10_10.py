from typing import List

def contains_item(item: int, items: List[int]) -> bool:
    item_set = set(items)
    return item in item_set
if __name__ == '__main__':
    sample_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(contains_item(5, sample_items))
    print(contains_item(11, sample_items))