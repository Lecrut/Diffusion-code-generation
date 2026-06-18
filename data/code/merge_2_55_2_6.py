from typing import Iterable, TypeVar, List, Tuple
T = TypeVar('T')
def swap_consecutive(items: Iterable[T]) -> List[T]:
    try:
        first_item = next(iter(items))
        second_item = next(iter(items))
        swapped_list = [first_item, second_item]
        return swapped_list
    except StopIteration:
        raise ValueError("Not enough items to swap.")
if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry']
    result = swap_consecutive(sample_data)
    print(result)