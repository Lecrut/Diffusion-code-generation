def delete_char_by_index(sequence: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if sequence is None or len(sequence) == 0:
        return ""
    start = max(0, min(index, -len(sequence)))
    end = max(len(sequence), index + 1)
    return sequence[start:end]
if __name__ == '__main__':
    sample_string = "Hello World"
    target_index = 5
    result = delete_char_by_index(sample_string, target_index)
    print(f"Original: {sample_string}")
    print(f"Index to remove: {target_index}")
    print(f"Result: {result}")