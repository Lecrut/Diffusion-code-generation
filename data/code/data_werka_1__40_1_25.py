def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    if not text.strip():
        raise ValueError("Input string cannot be empty or only whitespace")

def get_first_letters(text):
    validate_input(text)
    return [word[0] for word in text.split()]

if __name__ == '__main__':
    sample_string = "Alibaba Cloud provides innovative solutions"
    result = get_first_letters(sample_string)
    print(result)