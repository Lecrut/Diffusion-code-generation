import threading
from typing import Iterable
class CardinalityCalculator:
    def calculate_cardinality(self, iterable: Iterable) -> int:
        unique_elements = set(iterable)
        return len(unique_elements)
def main():
    calculator = CardinalityCalculator()
    sample_list = [1, 2, 3, 4, 5]
    sample_dict_keys = ['a', 'b', 'c'] * 10
    result_1 = calculator.calculate_cardinality(sample_list)
    result_2 = calculator.calculate_cardinality(sample_dict_keys)
    print(f"Cardinality of list: {result_1}")
    print(f"Cardinality of dict keys: {result_2}")
if __name__ == '__main__':
    main()