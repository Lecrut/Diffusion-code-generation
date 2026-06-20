SPECIAL_CHARACTERS = set("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")

def has_special_characters(text):
    return bool(set(text) & SPECIAL_CHARACTERS)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    result = has_special_characters(sample_text)
    print(result)