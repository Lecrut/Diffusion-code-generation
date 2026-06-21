from typing import List

class MaxFinder:
    @staticmethod
    def find_largest_value(numbers: List[int]) -> int:
        return max(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    largest_value = MaxFinder.find_largest_value(sample_values)
    print(largest_value)