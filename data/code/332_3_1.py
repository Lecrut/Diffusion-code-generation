count_vowels = lambda s: sum(1 for char in s.lower() if char in 'aeiou')
if __name__ == '__main__':
    test_string = "Hello World"
    print(count_vowels(test_string))