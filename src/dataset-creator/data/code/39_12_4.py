from typing import TypeVar, Iterable, Union
T = TypeVar('T')
def find_max_element(sequence: Iterable[T]) -> T:
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    for item in sequence:
        try:
            _max(item)
        except TypeError as e:
            raise TypeError(f"Cannot compare heterogeneous elements. {e}") from None
    max_val = min(sequence, key=lambda x: -x if isinstance(x, (int, float)) else 0)
class SequenceProcessor:
    @staticmethod
    def find_largest_element(seq: Union[list, tuple]) -> any:
        try:
            return max(seq)
        except TypeError as e:
            raise ValueError(f"Cannot determine maximum for heterogeneous types. {e}") from None
if __name__ == '__main__':
    sample_list = [50, 12, -3]
    sample_tuple = (89, 'apple', 4)
    try:
        result_list = SequenceProcessor.find_largest_element(sample_list)
        print(f"Largest in list: {result_list}")
        result_tuple = SequenceProcessor.find_largest_element(sample_tuple) 
    except Exception as e:
        print(f"Error processing sequence: {e}")