count_vowels = lambda text: sum(1 for c in text.lower() if c in 'aeiou')
if __name__ == '__main__':
    print(count_vowels("Hello World"))