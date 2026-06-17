import sys
from typing import Any, Callable, Iterable, List, Dict, TypeVar
T = TypeVar('T')
class DynamicCollectionCounter:
    def __init__(self):
        self._data_store: List[Any] = []
    def add(self, item: T) -> None:
        if not isinstance(item, (int, float)):
            try:
                int(item) or float(item)
            except ValueError:
                raise TypeError(f"Unsupported type {type(item).__name__} for numeric aggregation.")
        self._data_store.append(item)
    def count(self, predicate: Callable[[T], bool] = lambda x: True) -> int:
        return sum(1 for item in self._data_store if predicate(item))
    def aggregate_custom(self, func: Callable[[List[T]], T]) -> Any:
        filtered = [item for item in self._data_store]
        try:
            return func(filtered)
        except Exception as e:
            raise RuntimeError(f"Aggregation failed with function {func.__name__}: {str(e)}")
    def get_statistics(self, numeric_only: bool = True) -> Dict[str, Any]:
        stats = {}
        if not self._data_store and (numeric_only or len([x for x in self._data_store]) == 0):
            return stats
        values = [float(x) for x in self._data_store]
        if numeric_only:
            filtered_values = [v for v in values if isinstance(v, float)]
            if not filtered_values:
                return {}
            sorted_vals = sorted(filtered_values)
            stats['count'] = len(sorted_vals)
            stats['min'] = min(sorted_vals)
            stats['max'] = max(sorted_vals)
            stats['sum'] = sum(sorted_vals)
            stats['mean'] = sum(sorted_vals) / len(sorted_vals)
        else:
            all_values = [float(x) for x in self._data_store]
            if not all_values:
                return {}
            sorted_all = sorted(all_values)
            stats['count'] = len(sorted_all)
            stats['min'] = min(sorted_all)
            stats['max'] = max(sorted_all)
            stats['sum'] = sum(sorted_all)
            stats['mean'] = sum(sorted_all) / len(sorted_all)
        return stats
if __name__ == '__main__':
    counter = DynamicCollectionCounter()
    sample_data: List[Any] = [10, 25.5, "30", 40, -5, float("inf")]
    for item in sample_data:
        try:
            counter.add(item)
        except TypeError as e:
            print(f"Skipping invalid entry due to {e}")
    def safe_mean(values):
        if not values or any(v == float('inf') for v in values):
            return 0.0
        return sum(values) / len([v for v in values if not (v == float('inf'))])
    result = counter.aggregate_custom(safe_mean)
    print(f"Custom Aggregation Result: {result}")
    stats = counter.get_statistics()
    print("Statistics:", stats)