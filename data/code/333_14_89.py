import re
def get_initial_chars(text: str) -> str:
    return ''.join(word[0] for word in text.split())
if __name__ == '__main__':
    sample_text = "Hello world! This is a test string."
    result = get_initial_chars(sample_text)
    print(result)