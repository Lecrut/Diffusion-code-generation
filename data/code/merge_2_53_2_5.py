from typing import Iterable, TypeVar, Any
T = TypeVar('T')
def count_from_start(sequence: Iterable[T]) -> int:
    try:
        return len(list(sequence))
    except TypeError as e:
        raise TypeError(f"Input must be an iterable sequence, got {type(sequence).__name__}.") from e
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b', 'c')
    sample_string = "Python"
    result_list = count_from_start(sample_list)
    result_tuple = count_from_start(sample_tuple)
    result_string = count_from_start(sample_string)
    print(f"List count: {result_list}")                         
    print(f"Tuple count: {result_tuple}")                          
    print(f"String count: {result_string}")                           
    try:
        invalid_input = "not a list or iterable in this context for len check if not handled by conversion inside function logic but here we rely on internal iteration attempt which catches TypeError from non-iterable types like int"
        print(count_from_start(1234))                                                                                                                                                                                                                                                                                                                                                                                               
    except TypeError as te:
        print(f"Error caught correctly for non-iterable input: {te}")