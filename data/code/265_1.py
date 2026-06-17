def extract_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char in vowels:
            result += char
    return result
if __name__ == '__main__':
    sample_string1 = "Hello World"
    sample_string2 = "Programming is fun"
    sample_string3 = "AEIOUaeiou123"
    print(extract_vowels(sample_string1))
    print(extract_vowels(sample_string2))
    print(extract_vowels(sample_string3))