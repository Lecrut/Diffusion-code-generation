import numpy as np
def find_central_mark(sequence):
    if len(sequence) == 0:
        return None
    length = len(sequence)
    if length % 2 != 0:
        center_index = length // 2
    else:
        center_index = (length - 1) // 2
    return sequence[center_index]
if __name__ == '__main__':
    int_sequence = [10, 20, 30, 40, 50]
    float_sequence = [1.1, 2.2, 3.3, 4.4, 5.5]
    str_sequence = ['a', 'b', 'c', 'd']
    result_int = find_central_mark(int_sequence)
    print(f"Integer sequence center: {result_int}")
    result_float = find_central_mark(float_sequence)
    print(f"Float sequence center: {result_float}")
    result_str = find_central_mark(str_sequence)
    print(f"String sequence center: '{result_str}'")