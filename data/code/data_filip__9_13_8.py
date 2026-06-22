from typing import Optional

def trim_whitespace(text: Optional[str]) -> str:
    if text is None:
        return ""
    start = 0
    length = len(text)
    while start < length and text[start] <= ' ':
        start += 1
    end = length
    while end > start and text[end - 1] <= ' ':
        end -= 1
    return text[start:end]

if __name__ == '__main__':
    sample_1 = "   Hello World   "
    sample_2 = "\t\tPython Code\t\t"
    sample_3 = "NoSpacesHere"
    sample_4 = "   "
    sample_5 = None
    print(trim_whitespace(sample_1))
    print(trim_whitespace(sample_2))
    print(trim_whitespace(sample_3))
    print(trim_whitespace(sample_4))
    print(trim_whitespace(sample_5))