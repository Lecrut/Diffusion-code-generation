def count_vowels(s):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

if __name__ == '__main__':
    print(count_vowels('Hello World'))
    print(count_vowels('Python Programming'))
    print(count_vowels('AEIOU'))
    print(count_vowels('bcdfg'))