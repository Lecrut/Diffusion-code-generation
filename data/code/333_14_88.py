import re
def get_initial_characters(text: str) -> str:
    return ''.join(word[0] for word in text.split()) if text else ""
if __name__ == '__main__':
    sample_input = "Hello world! Python is great. Regular expressions are powerful."
    result = get_initial_characters(sample_input)
    print(result)