from typing import TypeVar, Iterable, Union, Sequence
T = TypeVar('T')
def find_largest_element(sequence: Sequence[Union[int, float]]) -> T:
    if not sequence:
        raise ValueError("Sequence cannot be empty.")
    for item in sequence:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Unsupported type {type(item).__name__} found. Only int and float are allowed.")
    return max(sequence)
if __name__ == '__main__':
    sample_list = [3, 5, -10, 2]
    sample_tuple = (4.5, 8.9, 1.2)
    result_list = find_largest_element(sample_list)
    print(f"Largest in list: {result_list}")
    result_tuple = find_largest_element(sample_tuple)
    print(f"Largest in tuple: {result_tuple}")