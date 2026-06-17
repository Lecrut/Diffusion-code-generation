from typing import Iterable, TypeVar, Any
T = TypeVar('T')
def count_from_start(sequence: Iterable[T]) -> int:
    try:
        for _ in sequence:
            pass
        return 0
    except TypeError:
        raise TypeError(f"Input must be an iterable (e.g., list, tuple, string), not {type(sequence).__name__}")
def _safe_length(iterable) -> int:
    try:
        return len(list(iterable)) if hasattr(iterable, '__len__') else 0
    except TypeError:
        raise TypeError(f"Input must be an iterable (e.g., list, tuple, string), not {type(iterable).__name__}")
def count_from_start_v2(sequence):
    try:
        return len(sequence)
    except TypeError:
        raise TypeError(f"Input must be an iterable (e.g., list, tuple, string), not {type(sequence).__name__}")
if __name__ == '__main__':
    test_cases = [
        ([10, 20, 30], "List of integers"),
        ("Hello World", "String with spaces"),
        ((True, False), "Tuple of booleans"),
        ({'a': 1, 'b': 2}, "Dictionary keys as iterable"),
        (range(5), "Range object"),
    ]
    for data, description in test_cases:
        try:
            result = count_from_start(data)
            print(f"{description}: {result}")
        except TypeError as e:
            print(f"Error processing {description}: {e}")