from typing import Sequence, TypeVar

T = TypeVar('T')

def get_third_item(items: Sequence[T]) -> T:
    if not isinstance(items, (list, tuple)):
        raise TypeError(f"Expected a sequence type, got {type(items).__name__}")
    
    length = len(items)
    if length < 3:
        raise ValueError(f"List must contain at least three items, but got {length}")
    
    return items[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_third_item(sample_list)
    print(result)