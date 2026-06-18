import threading
from typing import Iterable
class CardinalityCounter:
    def count(self, iterable: Iterable) -> int:
        unique_elements = set(iterable)
        return len(unique_elements)
def main():
    counter = CardinalityCounter()
    sample_list = [1, 2, 3, 4, 5]
    sample_iterable = iter([6, 7, 8])
    result_list = counter.count(sample_list)
    result_iter = counter.count(sample_iterable)
    print(f"Cardinality of list: {result_list}")
    print(f"Cardinality of iterable: {result_iter}")
if __name__ == '__main__':
    main()