import re
def get_initial_chars(s):
    words = re.findall(r'\b\w+', s)
    return ''.join(word[0] for word in words if word)
if __name__ == '__main__':
    sample_input = "Hello, World! Python is great. Regular expressions are powerful."
    result = get_initial_chars(sample_input)
    print(result)