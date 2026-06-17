import re
def get_initial_chars(text: str) -> str:
    words = text.split()
    return ''.join(word[0] for word in words if word)
if __name__ == '__main__':
    sample_input = "Hello World Python Programming is Fun and Awesome"
    result = get_initial_chars(sample_input)
    print(result)