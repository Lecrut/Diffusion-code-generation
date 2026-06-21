from typing import List

def find_largest(data: List[float]) -> float:
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list_one = [10.5, 4.2, 25.8, 8.3, 30.1]
    sample_list_two = [-5.1, -1.2, -10.3, -2.4]
    sample_list_three = [7.7]
    print(f"List 1: {sample_list_one}")
    print(f"Largest in List 1: {find_largest(sample_list_one)}")
    print("-" * 20)
    print(f"List 2: {sample_list_two}")
    print(f"Largest in List 2: {find_largest(sample_list_two)}")
    print("-" * 20)
    print(f"List 3: {sample_list_three}")
    print(f"Largest in List 3: {find_largest(sample_list_three)}")