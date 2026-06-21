def get_middle(sequence):
    length = len(sequence)
    if length == 0:
        return None
    if length % 2 == 0:
        middle_index = length // 2
        return sequence[middle_index], sequence[middle_index - 1]
    else:
        middle_index = length // 2
        return sequence[middle_index]

if __name__ == '__main__':
    list_even = [1, 2, 3, 4]
    list_odd = [1, 2, 3]
    string_even = "ab"
    string_odd = "abc"
    empty_list = []
    tuple_odd = (10, 20, 30)

    print(get_middle(list_even))
    print(get_middle(list_odd))
    print(get_middle(string_even))
    print(get_middle(string_odd))
    print(get_middle(empty_list))
    print(get_middle(tuple_odd))