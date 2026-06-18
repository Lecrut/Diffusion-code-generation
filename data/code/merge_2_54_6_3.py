import numpy as np
def find_central_mark(sequence):
    if len(sequence) == 0:
        return None
    length = len(sequence)
    if length % 2 != 0:
        mid_index = length // 2
    else:
        mid_index = (length - 1) // 2
    return sequence[mid_index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    sample_mixed = ['x', True, None, {'key': 'val'}]
    results = []
    center_list = find_central_mark(sample_list)
    results.append(("List", center_list))
    center_tuple = find_central_mark(sample_tuple)
    results.append(("Tuple", center_tuple))
    center_mixed = find_central_mark(sample_mixed)
    results.append(("Mixed List", center_mixed))
    for label, value in results:
        print(f"{label}: {value}")