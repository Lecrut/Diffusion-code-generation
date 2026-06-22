LAST_INDEX = -1

def get_last_element(sequence):
    if len(sequence) == 0:
        raise IndexError("sequence index out of range")
    return sequence[LAST_INDEX:]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    slice_result = get_last_element(sample_data)
    print(slice_result)