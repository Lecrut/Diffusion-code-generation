from typing import List

MAX_VALUE = float('-inf')

def find_largest(data: List[float]) -> float:
    if not data:
        raise ValueError("Input list cannot be empty")
    
    largest = MAX_VALUE
    for element in data:
        if element > largest:
            largest = element
    
    return largest

if __name__ == '__main__':
    sample_list_one = [10, 4, 25, 8, 30]
    print(f"List 1: {sample_list_one}")
    print(f"Largest in List 1: {find_largest(sample_list_one)}")
    
    sample_list_two = [-5, -1, -10, -2]
    print(f"List 2: {sample_list_two}")
    print(f"Largest in List 2: {find_largest(sample_list_two)}")