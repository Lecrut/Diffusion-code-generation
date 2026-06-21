from typing import TypeVar, Sequence, List

T = TypeVar('T')

def filter_out_elements(seq: Sequence[T], element_type: type) -> List[T]:
    result = [item for item in seq if not isinstance(item, element_type)]
    return result

if __name__ == '__main__':
    sample_sequence = [1, "hello", 3.14, True, [1, 2], "world", 42]
    type_to_filter = str
    filtered_sequence = filter_out_elements(sample_sequence, type_to_filter)
    print(filtered_sequence)