import re
def get_initial_chars(text: str) -> str:
    return ''.join(word[0] for word in text.split())
if __name__ == '__main':
    sample_text = "Hello World Python Programming"
    result = get_initial_chars(sample_text)
    print(result)

if __name__ == '__main__':
    pass
