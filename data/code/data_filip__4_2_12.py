def count_consonants(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in text:
        if char.isalpha() and char.lower() not in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string with 123 numbers."
    result = count_consonants(sample_string)
    print(result)