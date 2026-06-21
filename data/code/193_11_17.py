from typing import List
EMPTY_LIST_MSG = 'The list is empty.'

def calculate_sum(numbers: List[int]) -> int:
    return sum(numbers)
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    print(f'Sum of {sample_list1}: {calculate_sum(sample_list1)}')
    sample_list2 = [-5, 10, 15, -20]
    print(f'Sum of {sample_list2}: {calculate_sum(sample_list2)}')
    empty_list = []
    if not empty_list:
        print(EMPTY_LIST_MSG)
    else:
        print(f'Sum of {empty_list}: {calculate_sum(empty_list)}')