from typing import Any, List, Tuple, Union
def reverse_list(seq: List[Any]) -> List[Any]:
    seq.reverse()
    return seq
def reverse_tuple(seq: Tuple[Any, ...]) -> Tuple[Any, ...]:
    return (*seq[::-1],)
def reverse_string(seq: str) -> str:
    return seq[::-1]
def reverse_iterable(
    iterable: Union[List[Any], Tuple[Any, ...], str]
) -> Any:
    if isinstance(iterable, list):
        result = []
        for item in reversed(iterable):
            result.append(item)
        return result
    elif isinstance(iterable, tuple):
        return (*iterable[::-1],)
    else:       
        return iterable[::-1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "hello"
    reversed_list = reverse_list(sample_list)
    print(f"Reversed List: {reversed_list}")
    reversed_tuple = reverse_tuple(sample_tuple)
    print(f"Reversed Tuple: {reversed_tuple}")
    reversed_str = reverse_string(sample_string)
    print(f"Reversed String: '{reversed_str}'")
    mixed_input = [1, 2, 'x', (4, 5)]
    result_mixed = reverse_iterable(mixed_input)
    print(f"Mixed Input Reversed: {result_mixed}")