def concatenate_strings(s1: str, s2: str) -> str:
    return f"{s1}{s2}"
if __name__ == '__main__':
    string_one = "Hello"
    string_two = "World!"
    result = concatenate_strings(string_one, string_two)
    print(result)