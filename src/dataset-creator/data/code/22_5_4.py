import sys
def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(s):
        return s
    if sys.getsizeof(s) > 10**6:
        return s[:index] + s[index+1:]
    return s[:index] + s[index+1:]
if __name__ == '__main__':
    sample_string = "Hello, World!"
    index_to_delete = 5
    result = delete_char_at_index(sample_string, index_to_delete)
    print(f"Original: {sample_string}")
    print(f"Deleted char at index {index_to_delete}: '{result}'")