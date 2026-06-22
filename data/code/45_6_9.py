from functools import reduce

def find_minimum(lst):
    return reduce(lambda a, b: a if a < b else b, lst)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print(find_minimum(sample_list))