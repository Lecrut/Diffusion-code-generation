import re
def get_initial_chars(s: str) -> str:
    return ''.join(word[0] for word in s.split())
if __name__ == '__main__':
    sample_string = "Hello World Python Programming"
    result = get_initial_chars(sample_string)
    print(result)