def concatenate_strings(str1: str, str2: str) -> str:
    return f"{str1}{str2}"
if __name__ == '__main__':
    input_a = "Hello"
    input_b = "World"
    result = concatenate_strings(input_a, input_b)
    print(result)