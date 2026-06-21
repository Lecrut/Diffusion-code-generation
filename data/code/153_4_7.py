from typing import List

def item_exists(item: int, items: List[int]) -> bool:
    return item in items

if __name__ == '__main__':
    sample_item = 3
    sample_list = [1, 2, 3, 4, 5]
    print(item_exists(sample_item, sample_list))