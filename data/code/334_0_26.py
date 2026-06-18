def concatenate_strings(str1: str, str2: str) -> str:
    return f"{str1}{str2}"
if __name__ == '__main__':
    s_a = "Hello"
    s_b = "World"
    result = concatenate_strings(s_a, s_b)
    print(result)