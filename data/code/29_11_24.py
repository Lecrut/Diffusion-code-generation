def reverse_word(word):
    char_list = list(word)
    left, right = (0, len(char_list) - 1)
    while left < right:
        char_list[left], char_list[right] = (char_list[right], char_list[left])
        left += 1
        right -= 1
    reversed_word = ''.join(char_list)
    return reversed_word
if __name__ == '__main__':
    sample_values = ['hello', 'world', 'python', 'reverse']
    for value in sample_values:
        print(reverse_word(value))