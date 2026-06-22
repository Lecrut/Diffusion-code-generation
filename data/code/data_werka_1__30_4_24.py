def swap_even_odd_characters(s):
    s_list = list(s)
    length = len(s_list)
    
    for i in range(0, length - 1, 2):
        s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
    
    return ''.join(s_list)

if __name__ == '__main__':
    sample_string = "abcdefg"
    result = swap_even_odd_characters(sample_string)
    print(result)