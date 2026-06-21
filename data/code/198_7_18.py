from functools import reduce

def find_min(lst):
    return reduce(lambda a, b: a if a < b else b, lst)

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 10]
    print(find_min(sample_list))