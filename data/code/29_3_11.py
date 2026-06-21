VOWELS = set("aeiouAEIOU")

def count_vowels(strings):
    if not isinstance(strings, (list, tuple)):
        raise TypeError("Input must be a list or tuple of strings")
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements in the input must be strings")
    return sum([1 for text in strings for char in text if char in VOWELS])

if __name__ == '__main__':
    sample_strings = ['apple', 'banana', 'cherry', 'date']
    result = count_vowels(sample_strings)
    print(result)