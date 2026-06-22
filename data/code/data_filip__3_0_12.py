def remove_vowels(s):
    return "".join([c for c in s if c.lower() not in "aeiou"])

if __name__ == '__main__':
    print(remove_vowels("Hello World"))