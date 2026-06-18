def concatenate_strings(str1: str, str2: str) -> str:
    return f"{str1}{str2}"
if __name__ == '__main__':
    input_str_1 = "Hello"
    input_str_2 = ", World!"
    result = concatenate_strings(input_str_1, input_str_2)
    print(result)