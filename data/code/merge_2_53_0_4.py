from typing import List
def count_items(items: List) -> int:
    return sum(1 for _ in enumerate(items))
if __name__ == '__main__':
    sample_list = [0, 1, 'a', True]
    result = count_items(sample_list)
    print(f"Count: {result}")