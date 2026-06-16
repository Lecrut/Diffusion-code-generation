def delete_character_by_index(data: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if len(data) == 0:
        return ""
    if index < 0 or index >= len(data):
        raise IndexError(f"Index {index} is out of bounds for string of length {len(data)}.")
    return data[:index] + data[index+1:]
if __name__ == '__main__':
    sample_string = "Hello, World!"
    target_index = 5
    try:
        result = delete_character_by_index(sample_string, target_index)
        print(f"Original: {sample_string}")
        print(f"Index to remove: {target_index}")
        print(f"Result after deletion: {result}")
    except (TypeError, IndexError) as e:
        print(f"Error occurred: {e}")