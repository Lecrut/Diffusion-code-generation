from typing import Any, Sequence
def get_element_at_index(sequence: Sequence[Any], index: int) -> Any:
    return sequence[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    print(get_element_at_index(sample_list, 2))
    print(get_element_at_index(sample_tuple, 0))