import sys
def concatenate_strings(s1: str, s2: str) -> str:
    return f"{s1}{s2}"
if __name__ == '__main__':
    input_str_1 = "Hello"
    input_str_2 = "World"
    result = concatenate_strings(input_str_1, input_str_2)
    print(result)
    sys.exit(0)