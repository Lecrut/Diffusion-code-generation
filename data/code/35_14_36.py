def count_vowels(input_string):
    vowels = 'aeiou'
    return sum(1 for char in input_string.lower() if char in vowels)

if __name__ == '__main__':
    sample_input = "Hello, World!"
    result = count_vowels(sample_input)
    print(result)