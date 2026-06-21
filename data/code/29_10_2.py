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
        "AEIOU",
        "aeiou",
        "Python Programming",
        "",
        "12345!@#$%",
        "Brrr",
        "AaEeIiOoUu"
    ]
    for s in sample_strings:
        print(count_vowels(s))