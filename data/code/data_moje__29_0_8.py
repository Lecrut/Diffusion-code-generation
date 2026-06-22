def count_vowels(s):
    vowels = set('aeiouAEIOU')
    return sum(1 for c in s if c in vowels)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Python Programming"
    sample3 = "aeiouAEIOU"
    print(count_vowels(sample1))
    print(count_vowels(sample2))
    print(count_vowels(sample3))