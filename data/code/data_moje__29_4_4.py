def count_vowels(text):
    unique_chars = set(text.lower())
    vowels = set('aeiou')
    return len(unique_chars.intersection(vowels))

if __name__ == '__main__':
    sample_texts = [
        "Hello World",
        "AEIOU aeioe",
        "bcdfg",
        "Python is awesome!",
        "",
        "aEiOu"
    ]
    for text in sample_texts:
        print(count_vowels(text))