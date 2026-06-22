def reverse_word(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    char_list = list(word)
    length = len(char_list)
    
    def swap_elements(lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]

    for i in range(length // 2):
        swap_elements(char_list, i, length - i - 1)
    
    return ''.join(char_list)

if __name__ == '__main__':
    sample_word = 'reverse'
    try:
        print(reverse_word(sample_word))
    except ValueError as e:
        print(e)