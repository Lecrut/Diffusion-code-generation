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
    ]
    for item in sample_iterables:
        count = calculator.calculate(item)
        print(f"Cardinality of {item}: {count}")
if __name__ == '__main__':
    main()