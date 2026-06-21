def get_head(lst):
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    empty_list = []
    print(get_head(sample_list))
    print(get_head(empty_list))