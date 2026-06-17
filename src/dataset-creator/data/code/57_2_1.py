def get_element(sequence: list, index: int) -> any:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    length = len(sequence)
    adjusted_index = index + length
    return sequence[adjusted_index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_element(sample_list, -1))