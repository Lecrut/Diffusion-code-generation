def concatenate_strings(str1: str, str2: str) -> str:
    return f"{str1}{str2}"

if __name__ == '__main__':
    first_string = "Good morning, "
    second_string = "everyone!"
    result = concatenate_strings(first_string, second_string)
    print(result)