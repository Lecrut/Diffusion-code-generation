INDEX_MAP = {0: 'first', 1: 'second', 2: 'third'}

def extract_third_item(sequence):
    minimum_length = 3
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    if len(sequence) < minimum_length:
        raise IndexError("Insufficient items in sequence")
    return sequence[INDEX_MAP[2]]

if __name__ == '__main__':
    data_source = [0, 0, 999, 0]
    output = extract_third_item(data_source)
    print(output)