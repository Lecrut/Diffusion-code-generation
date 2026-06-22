count_vowels = lambda s: sum(1 for c in s.lower() if c in 'aeiou')
if __name__ == '__main__':
    text = "Hello World"
    print(count_vowels(text))