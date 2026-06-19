def find_first_letters_optimized(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    words = input_string.split()
    for word in words:
        if word:
            yield word[0]

if __name__ == '__main__':
    test_string_1 = "Welcome to the world of Python"
    print("Test 1:")
    try:
        for letter in find_first_letters_optimized(test_string_1):
            print(letter)
    except ValueError as e:
        print(e)

    test_string_2 = "   Extra spaces   at the beginning and end   "
    print("\nTest 2:")
    try:
        for letter in find_first_letters_optimized(test_string_2):
            print(letter)
    except ValueError as e:
        print(e)

    test_string_3 = ""
    print("\nTest 3:")
    try:
        for letter in find_first_letters_optimized(test_string_3):
            print(letter)
    except ValueError as e:
        print(e)

    test_string_4 = "SingleWord"
    print("\nTest 4:")
    try:
        for letter in find_first_letters_optimized(test_string_4):
            print(letter)
    except ValueError as e:
        print(e)

    invalid_input = 12345
    print("\nInvalid Input Test:")
    try:
        for letter in find_first_letters_optimized(invalid_input):
            print(letter)
    except ValueError as e:
        print(e)