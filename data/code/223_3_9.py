from functools import reduce

def find_max(lst):
    return reduce(lambda x, y: x if x > y else y, lst)

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_max(sample_list))