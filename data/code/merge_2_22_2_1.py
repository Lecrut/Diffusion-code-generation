import sys
def delete_by_index(string: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if not isinstance(string, str):
        raise TypeError("String argument must be of type str.")
    if index < 0 or index >= len(string):
        raise IndexError(f"Index {index} is out of range for string of length {len(string)}.")
    return string[:index] + string[index+1:]
if __name__ == '__main__':
    sample_string = "Python Programming"
    target_index = 6
    try:
        result = delete_by_index(sample_string, target_index)
        print(f"Original String: {sample_string}")
        print(f"Character at index {target_index}: '{sample_string[target_index]}'")
        print(f"Result after deletion: {result}")
    except (TypeError, IndexError) as e:
        print(f"Error occurred: {e}", file=sys.stderr)