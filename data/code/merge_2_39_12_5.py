from typing import TypeVar, Sequence, Union, Iterable, Generic, List
T = TypeVar('T', bound=Union[int, float])
class MaxFinder:
    @staticmethod
    def find_max(sequence: 'Iterable[T]') -> T:
        if not sequence:
            raise ValueError("Sequence cannot be empty.")
        try:
            return max(sequence)
        except TypeError as e:
            raise TypeError(f"Unsupported data types in sequence. All elements must support comparison operators (e.g., int, float).") from e
if __name__ == '__main__':
    sample_list = [3, 5, -10, 2]
    sample_tuple = ('a', 'b')                                                                                                                                                                                                                                  
    test_cases = [
        ([30, 25, 40], int),
        ((9.8, -3.2, 7.1), float),
        (['apple', 'banana', 'cherry'], str),
        ([[1,2],[3]], list)                                                                                                                                                                                                                                                   
    ]
    valid_cases = [
        ([30, 25, 40]),
        ((9.8, -3.2, 7.1), 'tuple'),
        (['apple', 'banana'], 'str_tuple')                                                  
    ]
    print("Testing MaxFinder.find_max")
    test_data = [
        ([30, 25, 40], "List of ints"),
        ((9.8, -3.2, 7.1), "Tuple of floats"),
        (['apple', 'banana'], "Tuple of strings")                                   
    ]
    for data, desc in test_data:
        try:
            result = MaxFinder.find_max(data)
            print(f"{desc}: {result}")
        except Exception as ex:
            print(f"{desc} Error: {ex}")