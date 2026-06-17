from typing import Callable, Iterable, List
def filter_elements(data: Iterable[int], predicate: Callable[[int], bool]) -> List[int]:
    return [item for item in data if predicate(item)]
def remove_even_numbers(numbers: List[int]) -> List[int]:
    return filter_elements(numbers, lambda x: x % 2 != 0)
if __name__ == '__main__':
    sample_data = [1, 4, 5, 8, 9]
    result = remove_even_numbers(sample_data)
    print(result)