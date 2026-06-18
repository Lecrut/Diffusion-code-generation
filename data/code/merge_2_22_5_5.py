import sys
def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(s):
        return s
    char_list = list(s)
    del char_list[index]
    return "".join(char_list)
if __name__ == '__main__':
    sample_string = "Hello, World!"
    index_to_delete = 7
    result = delete_char_at_index(sample_string, index_to_delete)
    print(f"Original: {sample_string}")
    print(f"After deleting character at index {index_to_delete}:")
    print(result)