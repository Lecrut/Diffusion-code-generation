def count_vowels(input_string):
    vowels = "aeiou"
    count = 0
    for char in input_string.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sample_input = "Hello, World!"
    print(count_vowels(sample_input))