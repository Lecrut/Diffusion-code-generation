def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello World! This is a sample text with some vowels."
    result = count_vowels(sample_text)
    print(result)