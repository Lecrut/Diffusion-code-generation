def swap_neighbors(s):
    s_list = list(s)
    length = len(s_list)
    for index in range(length - 1):
        next_index = index + 1
        s_list[index], s_list[next_index] = s_list[next_index], s_list[index]
    return "".join(s_list)

if __name__ == '__main__':
    input_string = "abcdef"
    swapped_string = swap_neighbors(input_string)
    print(swapped_string)