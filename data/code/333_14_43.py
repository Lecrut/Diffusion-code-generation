import re
def get_first_chars(s: str) -> str:
    words = s.split()
    if not words:
        return ""
    first_chars = [word[0] for word in words]
    return "".join(first_chars)
if __name__ == '__main__':
    sample_string = "Hello world, this is a test string."
    result = get_first_chars(sample_string)
    print(result)