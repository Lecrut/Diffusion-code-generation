import threading
from typing import Iterable
class CardinalityCounter:
    def count(self, iterable: Iterable) -> int:
        unique_elements = set(iterable)
        return len(unique_elements)
def main():
    counter = CardinalityCounter()
    sample_iterables = [
        list(range(10)),
        "hello world",
        {1, 2, 3},
        ["a", "b", "c"],
    ]
    for i, data in enumerate(sample_iterables):
        result = counter.count(data)
        print(f"Sample {i + 1}: Cardinality is {result}")
if __name__ == '__main__':
    main()