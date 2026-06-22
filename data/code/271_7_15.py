def count_character_types(text):
    if not text:
        return {'uppercase': 0, 'lowercase': 0, 'digits': 0, 'punctuation': 0}
    counts = {'uppercase': 0, 'lowercase': 0, 'digits': 0, 'punctuation': 0}
    for char in text:
        if char.isupper():
            counts['uppercase'] += 1
        elif char.islower():
            counts['lowercase'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        elif not char.isalnum():
            counts['punctuation'] += 1
    return counts
if __name__ == '__main__':
    sample_text = 'Hello, World! 123'
    result = count_character_types(sample_text)
    print(result)