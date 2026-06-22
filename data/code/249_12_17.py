from typing import List

def find_largest_item(items: List[int]) -> int:
    if not items:
        raise ValueError("List is empty")
    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item

if __name__ == '__main__':
    sample_items = [3, 5, 1, 2, 4]
    print(find_largest_item(sample_items))