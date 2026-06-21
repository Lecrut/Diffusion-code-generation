def append_lists(first_list, second_list):
    first_list.extend(second_list)

if __name__ == '__main__':
    sample_first = [1, 2, 3]
    sample_second = [4, 5, 6]
    append_lists(sample_first, sample_second)
    print(sample_first)