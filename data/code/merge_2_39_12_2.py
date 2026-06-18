from typing import TypeVar, Iterable, Union, Sequence
T = TypeVar('T')
def find_max_element(sequence: Union[Sequence[T], T]) -> T:
    if not sequence:
        raise ValueError("Input sequence cannot be empty.")
    try:
        max_val = next(iter(sequence))
        for item in sequence:
            if item > max_val:
                max_val = item
        return max_val
    except TypeError as e:
        raise ValueError(f"Cannot compare elements of heterogeneous data type. Error details: {e}")
if __name__ == '__main__':
    sample_list = [3, 5, -10, 2]
    sample_tuple = (42, 'a', True)
    try:
        result_list = find_max_element(sample_list)
        print(f"Largest in {sample_list}: {result_list}")
    except ValueError as ve:
        print(f"Validation Error: {ve}")