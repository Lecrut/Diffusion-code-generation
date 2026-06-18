import re
def get_initial_chars(text: str) -> str:
    return ''.join(word[0] for word in text.split())
if __name__ == '__main__':
    sample = "Hello world! Python is great."
    result = get_initial_chars(sample)
    print(result)