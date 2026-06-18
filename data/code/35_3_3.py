def count_vowels(s: str) -> int:
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

if __name__ == '__main__':
    test_strings = ["Hello, World!", "Python3", "", "Aeiou"]
    print([(s, count_vowels(s)) for s in test_strings])