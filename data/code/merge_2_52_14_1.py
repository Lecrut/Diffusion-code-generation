from typing import Sequence, TypeVar
T = TypeVar('T')
def get_last_item(sequence: Sequence[T]) -> T | None:
    try:
        return sequence[-1]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    if isinstance(result, int):
        print(f"The last item is: {result}")