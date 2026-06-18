def remove_at_index(sequence: list, index: int) -> list:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    return sequence[:index] + sequence[index+1:]
if __name__ == '__main__':
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    index_to_remove = 5
    result = remove_at_index(data, index_to_remove)
    print(result)