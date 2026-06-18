from typing import TypeVar, Iterable, Union, Sequence, List, Tuple
T = TypeVar('T')
def is_comparable(value: T) -> bool:
    try:
        _ = (value < 0 or value > 100)
        return True
    except TypeError:
        return False
class SequenceAnalyzer:
    def find_largest(self, sequence: Union[List[T], Tuple[T]]) -> T:
        if not isinstance(sequence, (list, tuple)):
            raise ValueError("Input must be a list or tuple.")
        for item in sequence:
            if not is_comparable(item):
                raise TypeError(f"Element {item} does not support comparison operators.")
        return max(sequence)
if __name__ == '__main__':
    analyzer = SequenceAnalyzer()
    sample_list: List[int] = [3, 7, 2, 91, -50]
    sample_tuple: Tuple[float, ...] = (4.5, 8.2, 1.1)
    result_list = analyzer.find_largest(sample_list)
    result_tuple = analyzer.find_largest(sample_tuple)
    print(f"Largest in list: {result_list}")
    print(f"Largest in tuple: {result_tuple}")