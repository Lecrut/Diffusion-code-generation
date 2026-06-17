from typing import TypeVar, Iterable, Sequence, Union, List, Tuple
T = TypeVar('T')
def find_largest_element(sequence: Union[List[T], Tuple[T]]) -> T:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be an instance of list or tuple.")
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty.")
    try:
        return max(sequence)
    except TypeError as e:
        raise TypeError(f"Cannot compare elements in the sequence. All elements must support comparison operators.") from e
if __name__ == '__main__':
    sample_list = [3, 50, -10, 2]
    sample_tuple = (42, 'a', True)                                                                                                                                                                                                                                                                                           
    valid_list = [10, 25, 3]
    valid_tuple = (99, 'apple', 'banana')                         
    print(f"Largest in list {valid_list}:")
    try:
        result_l = find_largest_element(valid_list)
        print(result_l)
    except Exception as e:
        print(e)
    print("\nLargest in tuple:")
    try:
        result_t = find_largest_element(valid_tuple)
        print(result_t)
    except Exception as e:
        print(e)
    try:
        find_largest_element([1, 2])
    except TypeError:
        pass
    try:
        find_largest_element([])
    except ValueError:
        pass
    mixed_comparable = [3.5, 'three', -1] 
    print(f"\nTesting heterogeneous comparable types (numbers and strings):")
    try:
        res = find_largest_element(mixed_comparable)
        print(res)
    except TypeError as te:
        pass
    safe_mixed = [10, 20]
    print(f"Largest in {safe_mixed}:")
    res_final = find_largest_element(safe_mixed)
    print(res_final)