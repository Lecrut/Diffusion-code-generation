def get_element(sequence: object, index: int) -> any:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    try:
        return sequence[index]
    except IndexError as e:
        raise IndexError(f"Index {index} out of range for the given sequence") from None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_element(sample_list, -1))