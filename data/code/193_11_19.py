from typing import List

def list_sum(numbers: List[int]) -> int:
    return sum(numbers)

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, -5, 20.5, 0],
        [],
        [100]
    ]
    
    for lst in sample_lists:
        print(f"Sum of {lst}: {list_sum(lst)}")