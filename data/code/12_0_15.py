def get_middle(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence must not be empty")
    middle_index = (length - 1) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4, 5, 6]
    single_element = [42]
    
    print(get_middle(odd_list))
    print(get_middle(even_list))
    print(get_middle(single_element))