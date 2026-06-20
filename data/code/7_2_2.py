SPECIAL_CHARACTERS = set('!@#$%^&*()_+-=[]{}|;:,.<>?/~`')

def has_special_characters(text):
    text_set = set(text)
    return bool(text_set & SPECIAL_CHARACTERS)

if __name__ == '__main__':
    sample_text_1 = "Hello World"
    sample_text_2 = "Hello@World!"
    print(has_special_characters(sample_text_1))
    print(has_special_characters(sample_text_2))