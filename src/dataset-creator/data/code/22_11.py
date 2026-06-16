def remove_at_index(sequence: list, index: int) -> list:
    return sequence[:index] + sequence[index+1:]
if __name__ == '__main__':
    sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    index_to_remove = 5
    result = remove_at_index(sample_list, index_to_remove)
    print(result)