def delete_by_index(sequence: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    length = len(sequence)
    if index < 0 or index >= length:
        raise IndexError(f"Index {index} is out of bounds for a sequence of length {length}.")
    return sequence[:index] + sequence[index+1:]
if __name__ == '__main__':
    sample_string = "Hello, World!"
    target_index = 7
    try:
        result = delete_by_index(sample_string, target_index)
        print(f"Original: {sample_string}")
        print(f"Deleted at index {target_index}:")
        print(result)
    except (TypeError, IndexError) as error:
        print(f"Error occurred during deletion: {error}")