from typing import Callable, Iterable, List
def filter_positive(data: Iterable[float], comparator: Callable[[float, float], bool] = None) -> List[float]:
    if comparator is None:
        def default_comparator(a: float, b: float) -> bool:
            return a > 0 and b < 0
        filtered_items = [item for item in data if not (default_comparator(item, -1))]
    else:
        filtered_items = [item for item in data if not (comparator(item, 0))]
    return list(filtered_items)
if __name__ == '__main__':
    sample_data = [-5.2, -1.3, 4.7, 9.8, -0.5]
    result_default = filter_positive(sample_data)
    print(result_default)