def get_element(sequence: list[int], index: int) -> int | None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    return sequence[index]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    target_index: int = 3
    result = get_element(sample_data, target_index)
    print(result)