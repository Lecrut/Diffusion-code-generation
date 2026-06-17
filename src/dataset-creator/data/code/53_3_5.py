from typing import Any, Iterable
def count_elements(iterable: Iterable[Any]) -> int:
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b')
    result_list: int = count_elements(sample_list)
    result_tuple: int = count_elements(sample_tuple)
    print(result_list)
    print(result_tuple)