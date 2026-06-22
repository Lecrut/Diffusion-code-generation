def find_first_letters_optimized(input_string):
    import re
    words = re.findall(r'\b\w', input_string)
    for word in words:
        yield word

if __name__ == '__main__':
    test_string_1 = "An example sentence with multiple words"
    print("Test 1:")
    for letter in find_first_letters_optimized(test_string_1):
        print(letter)
    
    test_string_2 = "   Leading and trailing spaces   "
    print("\nTest 2:")
    for letter in find_first_letters_optimized(test_string_2):
        print(letter)
    
    test_string_3 = "Singleword"
    print("\nTest 3:")
    for letter in find_first_letters_optimized(test_string_3):
        print(letter)