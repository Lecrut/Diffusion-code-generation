from typing import List

class MaxFinder:
    @staticmethod
    def find_largest(data: List[float]) -> float:
        if not data:
            raise ValueError("Input list cannot be empty")
        largest = max(data)
        return largest

if __name__ == '__main__':
    sample_list_one = [10.5, 4.2, 25.7, 8.3, 30.9]
    sample_list_two = [-5.5, -1.2, -10.8, -2.1]
    sample_list_three = [7.6]
    
    print(f"List 1: {sample_list_one}")
    print(f"Largest in List 1: {MaxFinder.find_largest(sample_list_one)}")
    print("-" * 20)
    print(f"List 2: {sample_list_two}")
    print(f"Largest in List 2: {MaxFinder.find_largest(sample_list_two)}")
    print("-" * 20)
    print(f"List 3: {sample_list_three}")
    print(f"Largest in List 3: {MaxFinder.find_largest(sample_list_three)}")