import str.translate

def count_vowels(text):
    translation_table = str.maketrans({
        'a': 'a', 'A': 'a',
        'e': 'e', 'E': 'e',
        'i': 'i', 'I': 'i',
        'o': 'o', 'O': 'o',
        'u': 'u', 'U': 'u'
    })
    normalized = text.translate(translation_table)
    count = 0
    for char in normalized:
        if char in "aeiou":
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Programming in Python is fun and effective for data science"
    result = count_vowels(sample_string)
    print(result)