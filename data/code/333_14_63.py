import re
def get_initial_chars(s: str) -> str:
    words = s.split()
    return ''.join(word[0] for word in words if word)
if __name__ == '__main__':
    sample_string = "Hello World Python Programming is Fun"
    result = get_initial_chars(sample_string)
    print(result)