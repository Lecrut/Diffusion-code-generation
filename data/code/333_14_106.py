import re
def get_first_letters(text: str) -> str:
    return ''.join(word[0] for word in text.split()) if text else ""
if __name__ == '__main__':
    sample_input = "Hello World Python Programming"
    result = get_first_letters(sample_input)
    print(result, end="")