def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    
    def swap_characters(chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    
    char_list = list(word)
    swap_characters(char_list, 0, len(char_list) - 1)
    return ''.join(char_list)

if __name__ == '__main__':
    sample_word = 'alibaba'
    try:
        print(reverse_word(sample_word))
    except ValueError as e:
        print(e)