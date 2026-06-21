import bisect

def get_central_value(lst):
    return lst[bisect.bisect_left(lst, 0) + (len(lst) - 1) // 2]

if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9]
    print(get_central_value(sample_list))