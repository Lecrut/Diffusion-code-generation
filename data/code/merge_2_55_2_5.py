from typing import TypeVar, Iterable, Iterator, Any, Tuple
T = TypeVar('T')
def swap_consecutive(iterable: Iterable[T]) -> bool:
    iterator = iter(iterable)
    try:
        first_item = next(iterator)
        second_item = next(iterator)
        lst = list(iterator) + [first_item] + [second_item]
        return True
    except StopIteration:
        return False
def main():
    sample_list = [10, 20, 30, 40, 50]
    if swap_consecutive(sample_list):
        print(f"Swapped successfully. New list: {sample_list}")
if __name__ == '__main__':
    main()