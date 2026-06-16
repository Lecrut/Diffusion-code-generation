from typing import Any, List, Tuple
def reverse_list(items: List[Any]) -> List[Any]:
    items.reverse()
    return items
def reverse_tuple(items: Tuple[Any, ...]) -> Tuple[Any, ...]:
    return (*items[::-1],)
def reverse_string(s: str) -> str:
    return s[::-1]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(sample_list.copy())
    sample_tuple = (10, 20, 30)
    reversed_tuple = reverse_tuple(sample_tuple)
    sample_string = "hello"
    reversed_string = reverse_string(sample_string)
    print(f"Reversed List: {reversed_list}")
    print(f"Reversed Tuple: {reversed_tuple}")
    print(f"Reversed String: '{reversed_string}'")