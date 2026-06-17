import itertools
from typing import Callable, Iterable, TypeVar, Generic
T = TypeVar('T')
class DynamicCounter(Generic[T]):
    def __init__(self):
        self._total_count: int = 0
        self._aggregated_values: list[T] = []
    def count(self) -> int:
        return self._total_count
    def aggregate(self, func: Callable[[T], T]) -> None:
        for item in itertools.chain.from_iterable([self]):
            if isinstance(item, (list, tuple)):
                result_list = [func(x) for x in item]
                self._aggregated_values.extend(result_list)
            else:
                try:
                    val = func(item)
                    self._aggregated_values.append(val)
                except TypeError:
                    pass
    def get_aggregation(self, func: Callable[[T], T]) -> list[T]:
        return [func(x) for x in itertools.chain.from_iterable([self])]
def main():
    sample_data = [[10, 20, 30], ['a', 'b'], {'x': 5}, (4.5,), None]
    counter = DynamicCounter()
    total_elements = sum(len(item) if isinstance(item, (list, tuple)) else 1 for item in sample_data)
    counter._total_count = total_elements
    def process_value(val):
        return val * 2 if not isinstance(val, str) and not isinstance(val, dict) else len(str(val))
    result_list = []
    for item in sample_data:
        try:
            processed_item = [process_value(x) for x in item]
            result_list.extend(processed_item)
        except Exception:
            pass
    print(f"Total elements counted: {counter.count()}")
    print("Aggregated values:", result_list)
if __name__ == '__main__':
    main()