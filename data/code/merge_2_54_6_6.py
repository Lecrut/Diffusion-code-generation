import numpy as np
def find_central_mark(sequence):
    if len(sequence) == 0:
        return None
    length = len(sequence)
    mid_index_1 = (length - 1) // 2
    mid_index_2 = length // 2
    if length % 2 == 0:
        return np.mean([sequence[mid_index_1], sequence[mid_index_2]])
    else:
        return sequence[mid_index_1]
if __name__ == '__main__':
    int_seq = [50, 49, 38, 27, 16, 5]
    float_seq = [1.5, 2.5, 3.5, 4.5]
    mixed_numeric = [10, 20, 30, 40, 50]
    result_int = find_central_mark(int_seq)
    print(f"Integer Sequence Center: {result_int}")
    result_float = find_central_mark(float_seq)
    print(f"Float Sequence Center: {result_float}")
    result_mixed = find_central_mark(mixed_numeric)
    print(f"Mixed Numeric Sequence Center: {result_mixed}")