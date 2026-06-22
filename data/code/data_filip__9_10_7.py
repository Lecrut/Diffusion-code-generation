import string

def remove_whitespace(text: str) -> str:
    if not text:
        return text
    left = 0
    while left < len(text) and text[left].isspace():
        left += 1
    right = len(text) - 1
    while right >= 0 and text[right].isspace():
        right -= 1
    if left > right:
        return ""
    return text[left : right + 1]

if __name__ == "__main__":
    sample_1 = "   Hello World   "
    sample_2 = "\n\t  Python Code  \t\n"
    sample_3 = "NoWhitespace"
    sample_4 = "   "
    sample_5 = ""

    print(remove_whitespace(sample_1))
    print(remove_whitespace(sample_2))
    print(remove_whitespace(sample_3))
    print(remove_whitespace(sample_4))
    print(remove_whitespace(sample_5))