def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello World"
    result = count_vowels(sample_string)
    print(result)
    another_string = "PYTHON Programming"
    result2 = count_vowels(another_string)
    print(result2)