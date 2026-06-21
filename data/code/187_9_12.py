from typing import List

MAX_VALUE: float = float('inf')

def find_largest(data: List[float]) -> float:
    if not data:
        raise ValueError("Input list cannot be empty")
    
    largest = -MAX_VALUE
    for element in data:
        if element > largest:
            largest = element
    
    return largest

if __name__ == '__main__':
    sample_list_1 = [10, 4, 25, 8, 30]
    sample_list_2 = [-5, -1, -10, -2]
    sample_list_3 = [7]
    sample_list_empty = []
    
    print(f"List 1: {sample_list_1}")
    print(f"Largest in List 1: {find_largest(sample_list_1)}")
    print("-" * 20)
    print(f"List 2: {sample_list_2}")
    print(f"Largest in List 2: {find_largest(sample_list_2)}")
    print("-" * 20)
    print(f"List 3: {sample_list_3}")
    print(f"Largest in List 3: {find_largest(sample_list_3)}")