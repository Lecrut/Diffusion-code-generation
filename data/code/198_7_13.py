from functools import reduce

def find_min(lst):
    return reduce(lambda a, b: a if a < b else b, lst)

if __name__ == '__main__':
    sample_list = [4, 2, 9, 7, 5]
    print(find_min(sample_list))