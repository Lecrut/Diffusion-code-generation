def remove_at_index(sequence: list, index: int) -> list:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    return sequence[:index] + sequence[index+1:]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60]
    remove_index = 3
    result_sequence = remove_at_index(sample_data, remove_index)
    print(result_sequence)