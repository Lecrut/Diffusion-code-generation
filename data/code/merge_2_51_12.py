from typing import Sequence
def get_first_element(sequence: Sequence) -> object:
    return next(iter(sequence), None)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    print(get_first_element(sample_list))
    sample_tuple = ('a', 'b', 'c')
    print(get_first_element(sample_tuple))
    empty_sequence: Sequence[int] = []
    result = get_first_element(empty_sequence)
    if result is None:
        print("Sequence was empty.")