import re
def get_initial_chars(text: str) -> str:
    words = [word for word in text.split() if word]
    return ''.join(word[0].lower() for word in words)
if __name__ == '__main__':
    sample_text = "Hello World! This is a Test."
    result = get_initial_chars(sample_text)
    print(result)