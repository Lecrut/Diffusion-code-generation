from functools import reduce

def find_min(lst):
    return reduce(lambda x, y: x if x < y else y, lst)

if __name__ == '__main__':
    sample_list = [4, 2, 9, 7, 5, 6]
    print(find_min(sample_list))