import re
def extract_initial_chars(text: str) -> str:
    return ''.join(word[0] for word in text.split())
if __name__ == '__main__':
    sample_text = "Hello World Python Programming"
    result = extract_initial_chars(sample_text)
    print(result)