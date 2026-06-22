def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    
    def reverse_in_place(char_list):
        left, right = 0, len(char_list) - 1
        while left < right:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
    
    char_list = list(word)
    reverse_in_place(char_list)
    return ''.join(char_list)

if __name__ == '__main__':
    sample_word = 'reverse'
    try:
        print(reverse_word(sample_word))
    except ValueError as e:
        print(e)