def get_last_element(lst):
    return next(reversed(lst))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_element(sample_list))