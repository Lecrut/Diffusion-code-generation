def remove_by_index(seq: list, index: int) -> list:
    return seq[:index] + seq[index+1:]
if __name__ == '__main__':
    sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_index = 5
    result = remove_by_index(sample.copy(), target_index)
    print(result)