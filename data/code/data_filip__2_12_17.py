def validate_palindrome(input_string):
    if input_string is None:
        return False
    
    left_index = 0
    right_index = len(input_string) - 1
    
    while left_index < right_index:
        while left_index < right_index and not input_string[left_index].isalnum():
            left_index += 1
        while left_index < right_index and not input_string[right_index].isalnum():
            right_index -= 1
        if left_index < right_index:
            if input_string[left_index].lower() != input_string[right_index].lower():
                return False
            left_index += 1
            right_index -= 1
    return True

if __name__ == '__main__':
    test_strings = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon",
        "12321",
        "123",
        ""
    ]
    for s in test_strings:
        result = validate_palindrome(s)
        print(result)