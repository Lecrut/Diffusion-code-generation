VOWELS = "aeiou"

def count_vowels(input_string):
    return sum(1 for char in input_string.lower() if char in VOWELS)

if __name__ == '__main__':
    sample_string = "The quick brown fox jumps over the lazy dog"
    result = count_vowels(sample_string)
    print(result)