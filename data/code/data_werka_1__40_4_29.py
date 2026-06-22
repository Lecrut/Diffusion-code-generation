def find_first_letters_optimized(input_string):
    def is_valid_word(word):
        return bool(word)

    words = input_string.split()
    for word in words:
        if is_valid_word(word):
            yield word[0]

if __name__ == '__main__':
    test_string_1 = "Efficient code generation by Alibaba Cloud"
    print("Test 1:")
    for letter in find_first_letters_optimized(test_string_1):
        print(letter)

    test_string_2 = "   Extra spaces are handled correctly   "
    print("\nTest 2:")
    for letter in find_first_letters_optimized(test_string_2):
        print(letter)

    test_string_3 = ""
    print("\nTest 3:")
    for letter in find_first_letters_optimized(test_string_3):
        print(letter)