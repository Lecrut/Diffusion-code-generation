def find_first_letters_optimized(input_string):
    def is_non_empty_word(word):
        return bool(word)

    words = input_string.split()
    for word in filter(is_non_empty_word, words):
        yield word[0]

if __name__ == '__main__':
    test_string_1 = "Diversity in programming languages"
    print("Test 1:")
    for letter in find_first_letters_optimized(test_string_1):
        print(letter)
    
    test_string_2 = "   Extra spaces   between words "
    print("\nTest 2:")
    for letter in find_first_letters_optimized(test_string_2):
        print(letter)
    
    test_string_3 = "Singleword"
    print("\nTest 3:")
    for letter in find_first_letters_optimized(test_string_3):
        print(letter)
    
    test_string_4 = ""
    print("\nTest 4:")
    for letter in find_first_letters_optimized(test_string_4):
        print(letter)