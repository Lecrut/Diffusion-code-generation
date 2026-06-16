def remove_at_index(sequence: list, index: int) -> list:
    return sequence[:index] + sequence[index+1:]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    target_index = 2
    result = remove_at_index(sample_data, target_index)
    print(result)