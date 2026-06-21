def min_float(lst):
    return min(float(x) for x in lst)

if __name__ == '__main__':
    sample_list = [3, 5.5, '2', -1, 0]
    print(min_float(sample_list))