def get_last_element(sequence):
    if len(sequence) == 0:
        raise IndexError("Sequence cannot be empty")
    return sequence[-1]

DEFAULT_SAMPLE_DATA = [100, 200, 300, 400, 500]

if __name__ == '__main__':
    data = DEFAULT_SAMPLE_DATA
    result = get_last_element(data)
    print(result)