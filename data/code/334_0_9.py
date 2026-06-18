def concatenate_strings(str1: str, str2: str) -> str:
    return f"{str1}{str2}"
if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World!"
    result = concatenate_strings(string_a, string_b)
    print(result)