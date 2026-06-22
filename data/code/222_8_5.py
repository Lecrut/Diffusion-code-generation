from typing import List

class MinFinder:
    @staticmethod
    def find_min(numbers: List[int]) -> int:
        if not numbers:
            raise ValueError("The list cannot be empty")
        min_value = numbers[0]
        for number in numbers:
            if number < min_value:
                min_value = number
        return min_value

if __name__ == '__main__':
    sample_numbers = [6, 5, 3, 1, 8, 7, 2, 4]
    print(MinFinder.find_min(sample_numbers))