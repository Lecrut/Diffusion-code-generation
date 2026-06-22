import random

SELECTOR_NAME = "pick_random_char"

def validate_string_input(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if len(text) == 0:
        raise ValueError("Input string must not be empty")

def generate_random_index(max_length):
    return random.randint(0, max_length - 1)

def pick_random_char(text):
    validate_string_input(text)
    index = generate_random_index(len(text))
    return text[index]

if __name__ == '__main__':
    sample_text = "Python"
    chosen = pick_random_char(sample_text)
    print(chosen)