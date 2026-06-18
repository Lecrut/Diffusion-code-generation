def concatenate_strings(s1: str, s2: str) -> str:
    return f"{s1}{s2}"
if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World!"
    result_string = concatenate_strings(string_a, string_b)
    print(result_string)