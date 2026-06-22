def count_vowels(text):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "AEIOU aeiou",
        "Rhythm",
        "Beautiful day!",
        "12345 !@#$%",
        "",
        "aEiOu",
        "PYTHON IS AWESOME"
    ]
    for s in sample_strings:
        print(count_vowels(s))