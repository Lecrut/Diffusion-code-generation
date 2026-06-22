import sys

def remove_whitespace(text: str) -> str:
    return text.strip()

if __name__ == '__main__':
    sample_string_1 = "   Hello World   "
    sample_string_2 = "\n\tPython Code\n\t"
    sample_string_3 = "NoExtraSpaces"
    print(remove_whitespace(sample_string_1))
    print(remove_whitespace(sample_string_2))
    print(remove_whitespace(sample_string_3))