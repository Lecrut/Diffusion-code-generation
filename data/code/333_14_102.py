import re
def get_initial_chars(s: str) -> str:
    words = re.findall(r'\w+', s.lower())
    return ''.join(word[0] for word in words if len(word) > 1)
if __name__ == '__main__':
    sample_input = "Hello World! This is a test String."
    result = get_initial_chars(sample_input)
    print(result)