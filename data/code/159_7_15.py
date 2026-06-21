from typing import List

class NumberFilter:
    @staticmethod
    def collect_odd_numbers(numbers: List[int]) -> List[int]:
        return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = NumberFilter.collect_odd_numbers(sample_list)
    print(result)