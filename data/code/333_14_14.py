import re
def get_initial_chars(text: str) -> str:
    words = text.split() if text else []
    initials = [word[0].lower() for word in words]
    return ''.join(initials)
if __name__ == '__main__':
    sample_text = "Hello World! This is a test string."
    result = get_initial_chars(sample_text)
    print(result)