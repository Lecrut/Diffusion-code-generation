vowel_count = lambda s: sum(c.lower() in 'aeiou' for c in s)

if __name__ == '__main__':
    text = "Hello World"
    print(vowel_count(text))