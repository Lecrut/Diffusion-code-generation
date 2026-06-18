from typing import Any, Iterable, List, Tuple
def reverse_string(s: str) -> str:
    return s[::-1]
def reverse_list(items: List[Any]) -> List[Any]:
    return items[::-1]
def reverse_tuple(data: Tuple[Any, ...]) -> Tuple[Any, ...]:
    return data[::-1]
def reverse_sequence(sequence: Iterable[Any]) -> List[Any]:
    return [item for item in reversed(sequence)]
if __name__ == '__main__':
    sample_string = "Python"
    sample_list = [1, 2, 3, 4]
    sample_tuple = ("apple", "banana")
    print(reverse_string(sample_string))
    print(reverse_list(sample_list))
    print(reverse_tuple(sample_tuple))
    print(reverse_sequence("world"))