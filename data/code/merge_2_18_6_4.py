from typing import Any, List, Tuple, Union
def reverse_list(items: List[Any]) -> List[Any]:
    items.reverse()
    return items
def reverse_tuple(items: Tuple[Any, ...]) -> Tuple[Any, ...]:
    return (*reversed(list(items)),)
def reverse_string(s: str) -> str:
    return s[::-1]
def reverse_iterable(iterable: Union[List[Any], Tuple[Any, ...]]) -> List[Any]:
    if isinstance(iterable, (list, tuple)):
        result = []
        for item in iter(reversed(list(iterable))):
            result.append(item)
        return result
    else:
        raise TypeError("Input must be a list or tuple.")
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    reversed_list = reverse_list(sample_list)
    print(f"Reversed List: {reversed_list}")
    reversed_tuple = reverse_tuple(sample_tuple)
    print(f"Reversed Tuple: {reversed_tuple}")
    reversed_string = reverse_string(sample_string)
    print(f"Reversed String: '{reversed_string}'")
    mixed_iterable = [10, 20, ('x', 'y')]
    reversed_mixed = reverse_iterable(mixed_iterable)
    print(f"Reversed Mixed Iterable: {reversed_mixed}")