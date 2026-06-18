def delete_char(s: str, index: int) -> str:
    if not isinstance(index, int):
        return s
    try:
        return s[:index] + s[index+1:]
    except IndexError:
        return s
if __name__ == '__main__':
    test_string = "Hello World"
    index_to_delete = 5
    result = delete_char(test_string, index_to_delete)
    print(f"Original: {test_string}")
    print(f"Deleted char at index {index_to_delete}:")
    print(result)
    invalid_index_test = -10
    result_invalid = delete_char("Python", invalid_index_test)
    print(f"\nInvalid Index Test (Index: {invalid_index_test}):")
    print(result_invalid)