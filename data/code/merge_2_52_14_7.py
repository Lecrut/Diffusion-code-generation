from typing import Sequence, TypeVar, Any
T = TypeVar('T')
def get_last_item(sequence: Sequence[T]) -> T:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    return sequence[-1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result: Any = get_last_item(sample_list)
    print(result)
    sample_tuple = ('a', 'b', 'c')
    result_tuple: str = get_last_item(sample_tuple)
    print(result_tuple)