def count_character_types(text):
    char_types = {'uppercase': 0, 'lowercase': 0, 'digits': 0, 'punctuation': 0}
    for char in text:
        if char.isupper():
            char_types['uppercase'] += 1
        elif char.islower():
            char_types['lowercase'] += 1
        elif char.isdigit():
            char_types['digits'] += 1
        else:
            char_types['punctuation'] += 1
    return char_types
if __name__ == '__main__':
    sample_text = 'Hello, World! 123'
    result = count_character_types(sample_text)
    print(result)