import re
def get_initial_characters(text: str) -> str:
    return ''.join(word[0] for word in text.split())
if __name__ == '__main__':
    sample_text = "Hello World Python Programming"
    result = get_initial_characters(sample_text)
    print(result)