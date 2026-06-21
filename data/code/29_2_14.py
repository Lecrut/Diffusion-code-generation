def count_vowels(text):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    samples = [
        "Hello World",
        "AEIOU",
        "aeiou",
        "",
        "12345!@#",
        "Python Programming",
        "Rhythm",
        "AeIoU aeiou"
    ]
    for sample in samples:
        print(count_vowels(sample))