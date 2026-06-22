def strip_vowels(text):
    vowels = set('aeiouAEIOU')
    return ''.join([char for char in text if char not in vowels])

if __name__ == '__main__':
    sample_texts = [
        "Hello World",
        "Python Programming",
        "AEIOU aeiou",
        "12345 !@#$%",
        ""
    ]

    for text in sample_texts:
        print(strip_vowels(text))