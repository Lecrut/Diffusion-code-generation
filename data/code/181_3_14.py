def extract_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(filter(vowels.__contains__, text))

if __name__ == '__main__':
    sample_text1 = "Hello World"
    sample_text2 = "Programming is fun"
    sample_text3 = "AEIOUaeiou123"
    result1 = extract_vowels(sample_text1)
    print(f"Vowels in '{sample_text1}': {result1}")
    result2 = extract_vowels(sample_text2)
    print(f"Vowels in '{sample_text2}': {result2}")
    result3 = extract_vowels(sample_text3)
    print(f"Vowels in '{sample_text3}': {result3}")