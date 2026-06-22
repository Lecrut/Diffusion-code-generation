from typing import List

class MaxFinder:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def find_maximum(self) -> int:
        if not self.numbers:
            return None
        current_max = self.numbers[0]
        for number in self.numbers[1:]:
            if number > current_max:
                current_max = number
        return current_max

if __name__ == '__main__':
    sample_numbers = [15, 7, 22, 3, 45, 10]
    finder = MaxFinder(sample_numbers)
    max_value = finder.find_maximum()
    print(max_value)