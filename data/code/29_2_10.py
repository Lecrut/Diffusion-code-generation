def count_vowels(text):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Python Programming",
        "",
        "12345!@#",
        "AEIOU aeiou"
    ]
    for s in sample_strings:
        result = count_vowels(s)
        print(result)