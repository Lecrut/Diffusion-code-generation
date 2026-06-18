from typing import Sequence
def get_first_element(sequence: Sequence) -> object:
    return next(iter(sequence), None)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b', 'c')
    print(get_first_element(sample_list))
    print(get_first_element(sample_tuple))