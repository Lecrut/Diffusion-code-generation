def get_median(sorted_list):
    length = len(sorted_list)
    if length == 0:
        return None
    middle_index = length // 2
    if length % 2 == 1:
        return sorted_list[middle_index]
    else:
        lower = sorted_list[middle_index - 1]
        upper = sorted_list[middle_index]
        return (lower + upper) / 2

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [1, 3, 5, 7]
    single_list = [42]
    empty_list = []

    print(get_median(odd_list))
    print(get_median(even_list))
    print(get_median(single_list))
    print(get_median(empty_list))