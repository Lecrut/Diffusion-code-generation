from typing import List

class NumberFinder:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers
    
    def find_largest_value(self) -> int:
        return max(self.numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    finder = NumberFinder(sample_values)
    print(finder.find_largest_value())