def count_vowels(text):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = ""
    sample3 = "Python Programming"
    sample4 = "12345!@#$%"
    sample5 = "AEIOU aeiou"

    print(count_vowels(sample1))
    print(count_vowels(sample2))
    print(count_vowels(sample3))
    print(count_vowels(sample4))
    print(count_vowels(sample5))