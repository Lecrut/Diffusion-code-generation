def delete_at_index(sequence: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return sequence[:index] + sequence[index+1:]
    except IndexError:
        pass
if __name__ == '__main__':
    input_sequence = "Hello World"
    target_index = 5
    if not (0 <= target_index < len(input_sequence)):
        raise ValueError(f"Index {target_index} is out of bounds for sequence '{input_sequence}'.")
    result = delete_at_index(input_sequence, target_index)
    print(result)