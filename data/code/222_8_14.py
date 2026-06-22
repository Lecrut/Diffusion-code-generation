from typing import List

class NumberProcessor:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers

    def find_min(self) -> int:
        return min(self.numbers)

if __name__ == '__main__':
    sample_numbers = [6, 2, 8, 4, 10]
    processor = NumberProcessor(sample_numbers)
    print(processor.find_min())