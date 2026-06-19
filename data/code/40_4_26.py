def find_first_letters_optimized(input_string):
    import re
    word_iter = re.finditer(r'\b\w', input_string)
    for match in word_iter:
        yield match.group()

if __name__ == '__main__':
    test_string_1 = "This is a sample string"
    print("Test 1:")
    for letter in find_first_letters_optimized(test_string_1):
        print(letter)
    
    test_string_2 = "  leading spaces and multiple    spaces "
    print("\nTest 2:")
    for letter in find_first_letters_optimized(test_string_2):
        print(letter)
    
    test_string_3 = ""
    print("\nTest 3:")
    for letter in find_first_letters_optimized(test_string_3):
        print(letter)