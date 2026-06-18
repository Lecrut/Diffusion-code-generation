def get_element(sequence: list[int], index: int) -> int | None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    return sequence[index]
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    print(get_element(data, 2))