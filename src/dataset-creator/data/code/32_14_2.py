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
        range(5),
    ]
    for data in sample_iterables:
        result = counter.count(data)
        print(f"Cardinality of {data}: {result}")
if __name__ == '__main__':
    main()