def is_long(word):
    return len(word) > 10

if __name__ == '__main__':
    test_word_one = "short"
    test_word_two = "thisisalongwordwithmorethanonehundredcharacters"
    test_word_three = "exactlytenchars"
    
    result_one = is_long(test_word_one)
    print(f"'{test_word_one}' is long: {result_one}")
    
    result_two = is_long(test_word_two)
    print(f"'{test_word_two}' is long: {result_two}")
    
    result_three = is_long(test_word_three)
    print(f"'{test_word_three}' is long: {result_three}")