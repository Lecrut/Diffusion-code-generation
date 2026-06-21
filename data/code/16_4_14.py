def get_first_element(sequence):
    if len(sequence) == 0:
        raise IndexError("Cannot get first element from an empty sequence.")
    return sequence[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    result = get_first_element(sample_list)
    print(result)