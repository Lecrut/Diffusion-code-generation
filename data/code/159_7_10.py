from typing import List

class NumberFilter:
    def collect_odd_numbers(self, numbers: List[int]) -> List[int]:
        return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_filter = NumberFilter()
    result = number_filter.collect_odd_numbers(sample_values)
    print(result)