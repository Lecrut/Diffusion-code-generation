from typing import List

def list_sum(numbers: List[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    print(f"Sum of {sample_list1}: {list_sum(sample_list1)}")
    
    sample_list2 = [-10, -20, 30, 40]
    print(f"Sum of {sample_list2}: {list_sum(sample_list2)}")
    
    empty_list = []
    print(f"Sum of {empty_list}: {list_sum(empty_list)}")