import threading
from typing import Iterable
class CardinalityCalculator:
    def calculate(self, iterable: Iterable) -> int:
        unique_elements = set(iterable)
        return len(unique_elements)
def main():
    calculator = CardinalityCalculator()
    sample_iterables = [
        list(range(10)),
        "hello world",
        {1, 2, 3},
        range(5),
        ["a", "b", "c"] * 4
    ]
    for i, data in enumerate(sample_iterables):
        result = calculator.calculate(data)
        print(f"Sample {i + 1}: Cardinality is {result}")
if __name__ == '__main__':
    main()