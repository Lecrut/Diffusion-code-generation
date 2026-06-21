VOWELS = frozenset('aeiouAEIOU')

def count_vowels(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return sum(1 for ch in text if ch in VOWELS)

if __name__ == '__main__':
    sample = "Python programming is fun!"
    print(count_vowels(sample))