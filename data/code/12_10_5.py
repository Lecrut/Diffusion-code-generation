def get_middle(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_middle(sample_list))

    sample_list_even = [10, 20, 30, 40]
    print(get_middle(sample_list_even))

    sample_list_empty = []
    print(get_middle(sample_list_empty))