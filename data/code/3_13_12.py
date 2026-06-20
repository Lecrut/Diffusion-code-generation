def filter_vowels(text):
    return ''.join(c for c in text if c.lower() not in 'aeiou')

if __name__ == '__main__':
    sample = "Hello World! This is a test string with vowels."
    result = filter_vowels(sample)
    print(result)

    sample2 = "Python Programming is fun!"
    result2 = filter_vowels(sample2)
    print(result2)

    sample3 = "AEIOU aeiou"
    result3 = filter_vowels(sample3)
    print(result3)