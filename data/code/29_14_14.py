def count_vowels(s):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "AEIOU",
        "bcdfg",
        "Python Programming",
        "12345!@#$%"
    ]
    for text in sample_strings:
        result = count_vowels(text)
        print(result)