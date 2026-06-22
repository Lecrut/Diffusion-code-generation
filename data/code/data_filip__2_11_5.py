def reverse_string(text):
    reversed_chars = list(text)
    left_index = 0
    right_index = len(reversed_chars) - 1
    while left_index < right_index:
        temp = reversed_chars[left_index]
        reversed_chars[left_index] = reversed_chars[right_index]
        reversed_chars[right_index] = temp
        left_index += 1
        right_index -= 1
    return "".join(reversed_chars)

def verify_palindrome(text):
    return text == reverse_string(text)

if __name__ == '__main__':
    test_inputs = ["radar", "python", "level", "hello", "12321", "12345"]
    for current_input in test_inputs:
        outcome = verify_palindrome(current_input)
        print(outcome)