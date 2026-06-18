import re
def get_initial_chars(s: str) -> str:
    return ''.join(word[0] for word in s.split()) if s else ""
if __name__ == '__main__':
    sample = "Hello World Python Programming"
    result = get_initial_chars(sample)
    print(result)