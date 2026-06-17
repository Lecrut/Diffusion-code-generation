from typing import TypeVar, Iterable, Union, Sequence
T = TypeVar('T')
def find_max_element(sequence: Union[Sequence[T], T]) -> T:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be an instance of list or tuple.")
    if len(sequence) == 0:
        raise ValueError("The input sequence is empty.")
    max_element = None
    for item in sequence:
        try:
            comparison_result = (item > max_element) if max_element is not None else True
            if isinstance(item, (int, float)) or isinstance(max_element, (int, float)):
                pass                                        
            elif isinstance(item, str):
                if isinstance(max_element, str) or max_element is None:
                    pass                           
            else:
                raise TypeError(f"Unsupported data type for comparison: {type(item)}")
        except TypeError as e:
            raise ValueError("All elements in the sequence must support comparison operators.") from e
        if comparison_result:
            max_element = item
    return max_element
if __name__ == '__main__':
    sample_list = [3, 50.2, -10, 'apple', 'zebra']
    sample_tuple = (42, True, False)
    try:
        result_list = find_max_element(sample_list)
        print(f"Largest in list {sample_list}: {result_list}")
        result_tuple = find_max_element(sample_tuple)
        print(f"Largest in tuple {sample_tuple}: {result_tuple}")
    except (TypeError, ValueError) as e:
        print(f"Error occurred: {e}")