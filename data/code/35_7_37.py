def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in input_string if char in vowels)

if __name__ == '__main__':
    sample_input = "Hello, World! 123"
    result = count_vowels(sample_input)
    print(result)