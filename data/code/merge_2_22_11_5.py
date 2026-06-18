def remove_at_index(sequence: list, index: int) -> list:
    return sequence[:index] + sequence[index+1:]
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    idx_to_remove = 2
    result = remove_at_index(data, idx_to_remove)
    print(result)