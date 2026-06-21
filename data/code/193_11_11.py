from typing import List

def calculate_total_sum(numbers: List[int]) -> int:
    return sum(numbers)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    print(f"Sum of {sample_list1}: {calculate_total_sum(sample_list1)}")
    
    sample_list2 = [10, -5, 20, 0]
    print(f"Sum of {sample_list2}: {calculate_total_sum(sample_list2)}")
    
    empty_list = []
    print(f"Sum of {empty_list}: {calculate_total_sum(empty_list)}")