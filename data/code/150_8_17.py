from typing import TypeVar, Sequence, List

T = TypeVar('T')

class GenericSequenceRemover:
    def remove_type(self, seq: Sequence[T], type_to_remove: type) -> List[T]:
        return [item for item in seq if not isinstance(item, type_to_remove)]

if __name__ == '__main__':
    remover = GenericSequenceRemover()
    sample_sequence = [1, "hello", 3.14, True, [1, 2], "world", 42]
    type_to_remove = int
    result = remover.remove_type(sample_sequence, type_to_remove)
    print(result)