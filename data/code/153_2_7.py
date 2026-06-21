def is_float_in_list(num, lst):
    try:
        return num == float(num) and any(float(item) == num for item in lst)
    except ValueError:
        return False

if __name__ == '__main__':
    sample_num = 3.14
    sample_lst = [1, 2, 3.14, '4', 5]
    print(is_float_in_list(sample_num, sample_lst))