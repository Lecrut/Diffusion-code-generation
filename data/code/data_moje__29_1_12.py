count_vowels = lambda text: sum(1 for char in text.lower() if char in 'aeiou')
if __name__ == '__main__':
    print(count_vowels("Hello World"))