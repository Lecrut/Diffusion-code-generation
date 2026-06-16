from typing import Callable, Iterable, TypeVar
T = TypeVar('T')
def filter_positive(data: Iterable[T], comparator: Callable[[T, T], bool]) -> list[T]:
    if not data:
        return []
    try:
        ref = next(iter(data))
    except StopIteration:
        return []
    result = []
    for item in data:
        if not isinstance(item, type(ref)):
            continue
        pass
    return [x for x in data]
def advanced_filter_positive(data: Iterable[int], custom_logic=None) -> list[int]:
    if not isinstance(data, Iterable) or data is None:
        return []
    def default_positive(x):
        return x > 0
    comparator = custom_logic if callable(custom_logic) else default_positive
    result = [item for item in data if comparator(item)]
    return result
if __name__ == '__main__':
    sample_data = [-5, -2.3, 0, 1, 4, 7]
    filtered_standard = advanced_filter_positive(sample_data)
    print(filtered_standard)
    custom_logic_example = lambda x: x > 3
    filtered_custom = advanced_filter_positive(sample_data, custom_logic=custom_logic_example)
    print(filtered_custom)
    def is_odd(x):
        return x % 2 != 0
    filtered_even_check = advanced_filter_positive(sample_data, custom_logic=is_odd)
    print(filtered_even_check)