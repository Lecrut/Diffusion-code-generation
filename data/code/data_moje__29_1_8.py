vowel_count = lambda s: sum(1 for c in s.lower() if c in 'aeiou')

if __name__ == '__main__':
    print(vowel_count("Hello World"))