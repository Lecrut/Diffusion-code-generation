def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    unique_chars = set(text.lower())
    intersection = unique_chars.intersection(vowels)
    return len(intersection)

if __name__ == '__main__':
    sample_text = "Hello World! This is a test."
    result = count_vowels(sample_text)
    print(result)