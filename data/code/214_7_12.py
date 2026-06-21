def min_float_value(lst):
    return min(float(x) for x in lst)

if __name__ == '__main__':
    sample_list = [3, 5.5, '2', -1, 0]
    print(min_float_value(sample_list))