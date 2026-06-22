def count_vowels(text):
    if not isinstance(text, str):
        return 0
    vowels = set('aeiouAEIOU')
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_strings = ["Hello World", "AEIOU", "", "1234", "Python 3.12", "rhythm", "aEiOu"]
    for s in sample_strings:
        result = count_vowels(s)
        print(f"{s}: {result}")