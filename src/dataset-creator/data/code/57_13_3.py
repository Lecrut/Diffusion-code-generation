import sys
from typing import Any, Union, Tuple, List
def get_element_at_index(data: Union[List[Any], Tuple[Any]], index: int) -> Any:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return data[index]
    except IndexError as e:
        print(f"Error: Index {index} out of range for sequence with length {len(data)}.", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    print("Sample List:", sample_list)
    print(f"Element at index -1: {get_element_at_index(sample_list, -1)}")
    try:
        result = get_element_at_index(sample_list, 5)
    except SystemExit as e:
        pass
    print("\nSample Tuple:", sample_tuple)
    print(f"Element at index 2 from tuple: {get_element_at_index(sample_tuple, 2)}")
    try:
        result = get_element_at_index(sample_list, -10)
    except SystemExit as e:
        pass
    print("\nAll tests completed.")