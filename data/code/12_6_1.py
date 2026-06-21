def get_center_element(sequence):
    length = len(sequence)
    if length == 0:
        return None
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return (sequence[length // 2 - 1], sequence[length // 2])

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    print(get_center_element(odd_list))
    even_tuple = (10, 20, 30, 40)
    print(get_center_element(even_tuple))
    single_element = [42]
    print(get_center_element(single_element))
    empty_list = []
    print(get_center_element(empty_list))