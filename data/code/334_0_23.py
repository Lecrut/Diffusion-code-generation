def concatenate_strings(str1: str, str2: str) -> str:
    return f"{str1}{str2}"
if __name__ == '__main__':
    input_str_a = "Hello"
    input_str_b = "World"
    result = concatenate_strings(input_str_a, input_str_b)
    print(result)