count_vowels = lambda s: sum(1 for c in s.lower() if c in 'aeiou')

if __name__ == '__main__':
    text = "Hello World"
    print(count_vowels(text))
    print(count_vowels("Programming is fun"))
    print(count_vowels("aeiou"))
    print(count_vowels("xyz"))