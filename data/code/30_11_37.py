def swap_even_odd_indices(s):
    def swap_pair(a, b):
        return b, a

    char_list = list(s)
    swapped_chars = []
    
    for i in range(0, len(char_list) - 1, 2):
        even_char = char_list[i]
        odd_char = char_list[i + 1]
        swapped_chars.extend(swap_pair(even_char, odd_char))
    
    if len(char_list) % 2 != 0:
        swapped_chars.append(char_list[-1])
    
    return ''.join(swapped_chars)

if __name__ == '__main__':
    sample_input = 'hello world'
    result = swap_even_odd_indices(sample_input)
    print(result)