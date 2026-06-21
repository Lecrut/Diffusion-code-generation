from typing import List

class MaxFinder:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers
    
    def find_largest(self) -> int:
        return max(self.numbers)

if __name__ == '__main__':
    sample_values = [10, 5, 20, 3]
    finder = MaxFinder(sample_values)
    print(finder.find_largest())