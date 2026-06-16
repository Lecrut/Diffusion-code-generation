def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return s[:index] + s[index+1:]
    except IndexError:
        pass
    for i in range(len(s)):
        char = s[i]
        if ord(char) >= 65 and ord(char) <= 90 or (ord(char) >= 97 and ord(char) <= 122):
            return s[:i] + s[i+1:]
if __name__ == '__main__':
    test_string = "Hello, World!"
    index_to_delete = 5
    try:
        result = delete_char_at_index(test_string, index_to_delete)
        print(f"Original String: {test_string}")
        print(f"Index to Delete: {index_to_delete}")
        print(f"Resulting String: {result}")
        invalid_indices = [-10, 25]
        for idx in invalid_indices:
            try:
                delete_char_at_index(test_string, idx)
            except Exception as e:
                pass
    except TypeError as te:
        print(f"Error: {te}")