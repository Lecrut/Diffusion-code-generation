def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello World! This is an example string with vowels."
    result = count_vowels(sample_string)
    print(result)