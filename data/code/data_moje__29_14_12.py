def count_vowels(s):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

if __name__ == '__main__':
    sample1 = "Hello World"
    print(count_vowels(sample1))

    sample2 = "Python Programming"
    print(count_vowels(sample2))

    sample3 = "aeiouAEIOU"
    print(count_vowels(sample3))

    sample4 = "bcdfg"
    print(count_vowels(sample4))

    sample5 = ""
    print(count_vowels(sample5))