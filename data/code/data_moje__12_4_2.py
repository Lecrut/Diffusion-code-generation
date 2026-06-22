def get_middle_value(sequence):
    length = len(sequence)
    if length == 0:
        return None
    if length % 2 == 1:
        mid_index = length // 2
        return sequence[mid_index]
    else:
        mid_right = length // 2
        mid_left = mid_right - 1
        val_left = sequence[mid_left]
        val_right = sequence[mid_right]
        return (val_left + val_right) / 2

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [1, 2, 4, 8]
    single = [42]
    empty = []
    
    print(get_middle_value(odd_list))
    print(get_middle_value(even_list))
    print(get_middle_value(single))
    print(get_middle_value(empty))