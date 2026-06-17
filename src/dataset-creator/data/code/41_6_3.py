import time
from typing import Any, Callable, Iterable, List, Optional, TypeVar
T = TypeVar('T')
class DynamicCounter:
    def __init__(self):
        self._data_store: dict[str, list] = {}
    def add(self, key: str, value: T) -> None:
        if key not in self._data_store:
            self._data_store[key] = []
        self._data_store[key].append(value)
    def count_elements(
        self, 
        keys: Optional[List[str]] = None, 
        aggregation_func: Callable[[Iterable], Any] | None = None
    ) -> dict[str, Any]:
        if keys is None:
            keys = list(self._data_store.keys())
        results = {}
        for key in keys:
            values = self._data_store.get(key, [])
            if aggregation_func is not None and len(values) > 0:
                try:
                    aggregated_value = aggregation_func(values)
                    results[key] = {
                        'count': len(values),
                        'aggregated': aggregated_value
                    }
                except Exception as e:
                    results[key] = {'error': str(e)}
            else:
                results[key] = {'count': len(values)}
        return results
def default_aggregation(items: Iterable[T]) -> T:
    if not items:
        raise ValueError("Aggregation failed on empty collection")
    first_item = next(iter(items))
    try:
        result = sum(map(lambda x: int(x), list(items)))
        return float(result) / len(list(items))
    except (ValueError, TypeError):
        return str(first_item)
if __name__ == '__main__':
    counter = DynamicCounter()
    sample_data = [10, 20, 30]
    string_keys = ['apple', 'banana']
    for item in sample_data:
        counter.add('numbers', item)
    for key in string_keys:
        counter.add(key, f"Item_{key}")
    start_time = time.time()
    results = counter.count_elements(keys=['numbers'], aggregation_func=default_aggregation)
    end_time = time.time()
    print(f"\nExecution Time: {end_time - start_time:.6f} seconds")
    for key, data in results.items():
        if 'error' not in data:
            print(f"Key '{key}': Count={data['count']}, Aggregated={data['aggregated']}")