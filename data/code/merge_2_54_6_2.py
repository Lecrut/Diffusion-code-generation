import numpy as np
def find_center_mark(data):
    if data is None:
        return 0
    try:
        arr = np.array(data)
        length = len(arr)
        if length == 0:
            return 0
        center_index = (length - 1) // 2
        return int(center_index)
    except Exception:
        raise ValueError("Input must be convertible to a sequence.")
if __name__ == '__main__':
    sample_ints = [1, 2, 3]
    sample_floats = [0.5, 1.7, 2.9, 4.1]
    sample_mixed = ['a', 'b', 'c']
    print(f"Center of {sample_ints}: ", find_center_mark(sample_ints))
    print(f"Center of {sample_floats}: ", find_center_mark(sample_floats))
    print(f"Center of {sample_mixed}: ", find_center_mark(sample_mixed))