def count_character_types(text):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    punctuation_count = 0
    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isspace():
            punctuation_count += 1
    return {'uppercase': uppercase_count, 'lowercase': lowercase_count, 'digits': digit_count, 'punctuation': punctuation_count}
if __name__ == '__main__':
    sample_text = 'Hello, World! 123'
    result = count_character_types(sample_text)
    print(result)