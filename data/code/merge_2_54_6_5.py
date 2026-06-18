import numpy as np
def find_central_mark(sequence):
    if len(sequence) == 0:
        return None
    n = len(sequence)
    try:
        central_index = int(np.floor(n / 2))
        return sequence[central_index]
    except (TypeError, IndexError):
        raise ValueError("Input must be a valid list-like structure.")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    result_list = find_central_mark(sample_list)
    result_tuple = find_central_mark(sample_tuple)
    print(f"Central mark of list: {result_list}")
    print(f"Central mark of tuple: {result_tuple}")