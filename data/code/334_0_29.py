import sys
def concatenate_strings(str1: str, str2: str) -> str:
    return f"{str1}{str2}"
if __name__ == '__main__':
    sample_str_1 = "Hello"
    sample_str_2 = "World!"
    result = concatenate_strings(sample_str_1, sample_str_2)
    print(result)
    sys.exit(0)