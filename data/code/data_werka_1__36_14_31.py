def reverse_string_in_place(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')
    char_list = list(s)
    left, right = (0, len(char_list) - 1)
    while left < right:
        char_list[left], char_list[right] = (char_list[right], char_list[left])
        left += 1
        right -= 1
    return ''.join(char_list)
if __name__ == '__main__':
    test_cases = {'hello': 'olleh', 'Python': 'nohtyP', '': '', 'A man, a plan, a canal, Panama': 'amanaP ,lanac a ,nalp a ,nam A'}
    for input_str, expected_output in test_cases.items():
        result = reverse_string_in_place(input_str)
        print(f'Input: {input_str}')
        print(f'Reversed: {result}')
        assert result == expected_output, f'Test failed for input: {input_str}'