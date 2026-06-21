def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    unique_chars = set(text)
    found_vowels = unique_chars & vowels
    return len(found_vowels)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_vowels(sample_text)
    print(result)