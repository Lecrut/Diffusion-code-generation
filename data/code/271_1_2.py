def character_type_analyzer(text):
    counts = {
        'vowels': 0,
        'consonants': 0,
        'other': 0
    }
    vowels = "aeiouAEIOU"
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            if char in vowels:
                counts['vowels'] += 1
            else:
                counts['consonants'] += 1
        else:
            counts['other'] += 1
    return counts
if __name__ == '__main__':
    sample_string = "Hello World 123!"
    result = character_type_analyzer(sample_string)
    print(result)