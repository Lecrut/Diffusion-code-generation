from typing import Sequence
def get_first_element(sequence: Sequence) -> object:
    return next(iter(sequence), None)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b', 'c')
    result_list = get_first_element(sample_list)
    result_tuple = get_first_element(sample_tuple)
    print(f"First element of list: {result_list}")
    print(f"First element of tuple: {result_tuple}")