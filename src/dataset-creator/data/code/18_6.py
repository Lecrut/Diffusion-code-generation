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
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    print(reverse_list(sample_list))
    print(reverse_tuple(sample_tuple))
    print(reverse_string(sample_string))