from typing import Any, Iterable, TypeVar
def find_first_element(data: Any) -> Any:
    if data is None:
        raise ValueError("Input cannot be None.")
    def _get_first(iterable_obj):
        try:
            it = iter(iterable_obj)
            return next(it)
        except StopIteration:
            pass
    try:
        iter(data)
    except TypeError:
        pass
    if hasattr(data, '__len__') or isinstance(data, (str, bytes)):
        try:
            it = iter(data)
            return next(it)
        except StopIteration:
            raise ValueError("Provided container was empty and no elements exist to retrieve.")
    else:
        if data is not None:
            return data
        else:
            raise ValueError("Input must be non-None and either an iterable or a valid scalar.")
    if not isinstance(data, (list, tuple, set)):
        try:
            iter_data = iter(data)
        except TypeError:
            raise TypeError(f"Input must be an iterable or a single value; received {type(data).__name__} which is neither.")
    try:
        item = next(iter_data)
    except StopIteration:
        raise ValueError("The provided container was empty.")
    return item
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 'a', True], "List"),
        ((4,), "Tuple"),
        ({'z': 10}, "Dict (keys iteration)"),
        ("hello", "String"),
        ([], "Empty List - Should Raise"),
    ]
    for data, label in test_cases:
        try:
            result = find_first_element(data)
            print(f"{label}: {result}")
        except ValueError as e:
            print(f"{label}: Error -> {e}")