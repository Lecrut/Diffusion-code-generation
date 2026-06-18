import re
def get_initial_chars(s: str) -> str:
    matches = [word[0] for word in s.split() if word.strip()]
    return ''.join(matches)
if __name__ == '__main':
    sample_string = "Hello, world! This is a test string. Python 3."
    result = get_initial_chars(sample_string)
    print(result)

if __name__ == '__main__':
    pass
