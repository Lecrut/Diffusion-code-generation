def reverse_string_iterative(s):
    char_list = list(s)
    left, right = (0, len(char_list) - 1)
    while left < right:
        char_list[left], char_list[right] = (char_list[right], char_list[left])
        left += 1
        right -= 1
    return ''.join(char_list)
if __name__ == '__main__':
    sample_string = 'hello'
    reversed_string = reverse_string_iterative(sample_string)
    print(reversed_string)