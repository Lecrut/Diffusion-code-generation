import threading
from typing import Iterable
class CardinalityCounter:
    def count(self, iterable: Iterable) -> int:
        unique_elements = set(iterable)
        return len(unique_elements)
def main():
    counter = CardinalityCounter()
    sample_data_1 = [1, 2, 3, 4, 5]
    sample_data_2 = ['a', 'b', 'c'] * 10
    result_1 = counter.count(sample_data_1)
    result_2 = counter.count(sample_data_2)
    print(f"Cardinality of first iterable: {result_1}")
    print(f"Cardinality of second iterable: {result_2}")
if __name__ == '__main__':
    main()