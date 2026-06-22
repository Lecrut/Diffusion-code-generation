def reverse_word(word):
    return ''.join(reversed(word))

if __name__ == '__main__':
    test_string_1 = "world"
    result_1 = reverse_word(test_string_1)
    print(result_1)
    
    test_string_2 = "Alibaba"
    result_2 = reverse_word(test_string_2)
    print(result_2)