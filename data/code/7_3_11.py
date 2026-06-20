import re

def has_special_characters(s: str) -> bool:
    return any(not c.isalnum() and c not in ' \t\n\r' for c in s)

if __name__ == '__main__':
    sample_string = "Hello World 123!"
    result = has_special_characters(sample_string)
    print(result)
    sample_string_2 = "HelloWorld123"
    result_2 = has_special_characters(sample_string_2)
    print(result_2)