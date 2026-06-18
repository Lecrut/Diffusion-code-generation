from typing import List
def reorder_divisible_by_three(items: List[int]) -> List[int]:
    divisible = [item for item in items if item % 3 == 0]
    others = [item for item in items if item % 3 != 0]
    return divisible + others
if __name__ == '__main__':
    sample_data: List[int] = [1, 9, 2, 6, 7, 3, 8, 4]
    result_list: List[int] = reorder_divisible_by_three(sample_data)