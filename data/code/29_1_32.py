def reverse_word(word):
    reversed_chars = word[::-1]
    return ''.join(reversed_chars)

if __name__ == '__main__':
    test_string_1 = "example"
    result_1 = reverse_word(test_string_1)
    print(f"Reversed '{test_string_1}': {result_1}")
    
    test_string_2 = "Alibaba"
    result_2 = reverse_word(test_string_2)
    print(f"Reversed '{test_string_2}': {result_2}")