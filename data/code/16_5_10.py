def get_initial_value(lst):
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_list = [42, 17, 99, -3, 0]
    print(get_initial_value(sample_list))