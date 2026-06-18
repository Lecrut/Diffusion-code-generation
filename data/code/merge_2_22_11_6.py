def remove_at_index(sequence: list, index: int) -> list:
    if 0 <= index < len(sequence):
        return sequence[:index] + sequence[index+1:]
    raise IndexError("Index out of range")
if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    index_to_remove = 2
    result = remove_at_index(sample_sequence, index_to_remove)
    print(result)