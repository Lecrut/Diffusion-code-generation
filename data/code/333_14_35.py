import re
def get_initial_chars(s: str) -> str:
    return ''.join(word[0] for word in s.split())
if __name__ == '__main__':
    sample = "hello world this is a test string"
    result = get_initial_chars(sample)
    print(result)