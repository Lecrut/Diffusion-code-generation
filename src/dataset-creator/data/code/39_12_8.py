from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def find_max_element(sequence: Iterable[T]) -> T | None:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be an instance of list or tuple.")
    try:
        max_val = next(iter(sequence))
    except StopIteration:
        return None
    for item in sequence[1:]:
        try:
            if item > max_val:
                max_val = item
        except TypeError:
            continue
    return max_val
if __name__ == '__main__':
    sample_list = [3.14, "apple", 200]
    sample_tuple = ("banana", -5)
    result_list = find_max_element(sample_list)
    result_tuple = find_max_element(sample_tuple)
    print(f"Largest in list: {result_list}")
    print(f"Largest in tuple: {result_tuple}")