from typing import List, TypeVar, Any
T = TypeVar('T')
def extend_list(lst: List[T], items: tuple) -> None:
    if not isinstance(items, (list, tuple)):
        raise TypeError("Extension must be a sequence of compatible types.")
    for item in items:
        try:
            lst.append(item)
        except Exception as e:
            raise RuntimeError(f"Failed to extend list due to type mismatch or error: {e}") from None
if __name__ == '__main__':
    data = [1, 2, 3]
    test_cases = (4.5, "hello", True)
    try:
        extend_list(data, test_cases)
        print(f"Extended list successfully to: {data}")
        assert isinstance(data[0], int), "First element should be integer."
        assert isinstance(data[-1], str), "Last added element should be string."
    except Exception as e:
        print(f"Error occurred during extension: {e}")