def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_text = "Hello World! This is an optimized Python script."
    result = count_vowels(sample_text)
    print(result)