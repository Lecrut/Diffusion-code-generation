def get_element(sequence: list[int], index: int) -> int | None:
    return sequence[index] if 0 <= index < len(sequence) else None
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    print(get_element(data, 2))