def swap_neighbors(s):
    if len(s) < 2:
        return s
    
    char_list = list(s)
    swapped_list = []
    
    for i in range(0, len(char_list), 2):
        if i + 1 < len(char_list):
            swapped_list.append(char_list[i + 1])
        swapped_list.append(char_list[i])
    
    return ''.join(swapped_list)

if __name__ == '__main__':
    sample_string = "hello world"
    result = swap_neighbors(sample_string)
    print(result)