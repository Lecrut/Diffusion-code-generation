def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        raise IndexError("Sequence must not be empty")
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return sequence[length // 2 - 1]

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [10, 20, 30, 40]
    single_element_list = [42]
    
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))
    print(get_middle_element(single_element_list))