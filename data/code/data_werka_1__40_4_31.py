def find_first_letters_optimized(input_string):
    for word in input_string.split():
        yield word[0]

if __name__ == '__main__':
    sample_input = "This is a sample string with several words"
    first_letters = list(find_first_letters_optimized(sample_input))
    print(first_letters)