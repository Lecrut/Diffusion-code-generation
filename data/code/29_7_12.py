def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "AEIOUaeiou"
    sample3 = "Python Programming"
    print(count_vowels(sample1))
    print(count_vowels(sample2))
    print(count_vowels(sample3))