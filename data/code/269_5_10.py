def find_unique_punctuation(text):
    punctuation = set()
    for char in text:
        if not char.isalnum():
            punctuation.add(char)
    return list(punctuation)

if __name__ == '__main__':
    sample_string1 = "Hello, world! This is a test string."
    sample_string2 = "Python3.10 is great!"
    sample_string3 = "NoPunctuationHere"
    sample_string4 = "!@#$%^&*()_+=-`~"

    result1 = find_unique_punctuation(sample_string1)
    print(f"String: '{sample_string1}'")
    print(f"Punctuation: {result1}")

    result2 = find_unique_punctuation(sample_string2)
    print(f"String: '{sample_string2}'")
    print(f"Punctuation: {result2}")