from typing import Iterable, TypeVar, Optional
T = TypeVar('T')
def get_last_element(iterable: Iterable[T]) -> Optional[T]:
    try:
        iterator = iter(iterable)
        last_item = None
        for item in iterator:
            last_item = item
        return last_item
    except TypeError:
        raise
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_last_element(sample_list)
    if result is None:
        print("The sequence was empty.")
    else:
        print(f"The last element is {result}")