def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char.isalpha() and char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_input = "Hello, World! 123"
    result = count_vowels(sample_input)
    print(result)