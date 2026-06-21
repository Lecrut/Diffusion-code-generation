def count_vowels(s):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    print(count_vowels("Hello World"))
    print(count_vowels("Python Programming"))
    print(count_vowels(""))
    print(count_vowels("12345!@#$%"))
    print(count_vowels("AEIOU"))
    print(count_vowels("bcdfg"))