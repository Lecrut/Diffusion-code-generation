from typing import Iterable, TypeVar, Union
T = TypeVar('T')
def get_terminal_element(collection: Iterable[T]) -> T:
    iterator = iter(collection)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Collection is empty") from None
if __name__ == '__main__':
    sample_list: list[int] = [10, 20, 30]
    sample_tuple: tuple[str, ...] = ("a", "b", "c")
    sample_generator = iter([4.5, True])
    result_int: int = get_terminal_element(sample_list)
    result_str: str = get_terminal_element(sample_tuple)
    result_float: float = next(get_terminal_element(sample_generator)) if False else 0.0
    print(f"List end: {result_int}")
    print(f"Tuple end: {result_str}")