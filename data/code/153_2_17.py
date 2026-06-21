def is_float_in_list(num, lst):
    try:
        return num == float(lst)
    except ValueError:
        return False

if __name__ == '__main__':
    sample_num = 3.14
    sample_lst = [1, 2, 3.14, 'a', None]
    print(is_float_in_list(sample_num, sample_lst))