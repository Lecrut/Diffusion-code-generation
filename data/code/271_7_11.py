def count_character_types(text):
    UPPER = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    LOWER = set('abcdefghijklmnopqrstuvwxyz')
    DIGITS = set('0123456789')
    PUNCTUATION = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    upper_count = 0
    lower_count = 0
    digit_count = 0
    punctuation_count = 0
    for char in text:
        if char in UPPER:
            upper_count += 1
        elif char in LOWER:
            lower_count += 1
        elif char in DIGITS:
            digit_count += 1
        elif char in PUNCTUATION:
            punctuation_count += 1
    return {'uppercase': upper_count, 'lowercase': lower_count, 'digits': digit_count, 'punctuation': punctuation_count}
if __name__ == '__main__':
    result = count_character_types('Hello, World! 123')
    print(result)