from functools import reduce

def min_value(lst):
    return reduce(lambda a, b: a if a < b else b, lst)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(min_value(sample_list))