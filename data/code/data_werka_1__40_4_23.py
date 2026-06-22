def find_first_letters_optimized(input_string):
    for word in input_string.split():
        if word:
            yield word[0]

if __name__ == '__main__':
    test_strings = [
        "This is a sample string",
        "  leading spaces and multiple    spaces ",
        "",
        "singleword"
    ]
    
    for i, test_string in enumerate(test_strings):
        print(f"Test {i+1}:")
        for letter in find_first_letters_optimized(test_string):
            print(letter)
        print()