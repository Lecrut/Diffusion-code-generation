from typing import Sequence, TypeVar

T = TypeVar('T')

def get_final_entry(collection: Sequence[T]) -> T:
    if not collection:
        raise ValueError("Collection is empty")
    iterator = iter(collection)
    last_item: T = iterator.__next__()
    for item in iterator:
        last_item = item
    return last_item

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    result = get_final_entry(sample_list)
    print(result)