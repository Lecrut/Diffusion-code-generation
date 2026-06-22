def reverse_word(s):
    char_list = list(s)
    left, right = 0, len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    return ''.join(char_list)

if __name__ == '__main__':
    test_string1 = "hello"
    result1 = reverse_word(test_string1)
    print(f"'{test_string1}' reversed is '{result1}'")
    
    test_string2 = "world"
    result2 = reverse_word(test_string2)
    print(f"'{test_string2}' reversed is '{result2}'")
    
    test_string3 = "Python"
    result3 = reverse_word(test_string3)
    print(f"'{test_string3}' reversed is '{result3}'")