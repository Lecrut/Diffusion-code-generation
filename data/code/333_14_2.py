import re
def get_initial_chars(s: str) -> str:
    words = s.split()
    if not words:
        return ""
    initials = [word[0].upper() for word in words]
    return "".join(initials)
if __name__ == '__main__':
    sample_string = "hello world, this is a test string."
    result = get_initial_chars(sample_string)
    print(result)