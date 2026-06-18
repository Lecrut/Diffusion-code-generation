from typing import List, Optional
class MaxValueFinder:
    def find_maximum(self, numbers: List[float]) -> float:
        if not isinstance(numbers, list):
            raise TypeError("Input must be a list.")
        for item in numbers:
            if not isinstance(item, (int, float)):
                raise ValueError(f"All elements must be numeric. Got {type(item).__name__}.")
            if len(numbers) == 0:
                raise ValueError("The input list cannot be empty.")
        return max(numbers)
if __name__ == '__main__':
    finder = MaxValueFinder()
    sample_data_1 = [3.5, -2.7, 8.9, 4.1]
    result_1 = finder.find_maximum(sample_data_1)
    sample_data_2 = [-10, -5, -20, -1]
    result_2 = finder.find_maximum(sample_data_2)
    print(f"Maximum of {sample_data_1}: {result_1}")
    print(f"Maximum of {sample_data_2}: {result_2}")