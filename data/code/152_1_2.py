import time
def find_intersection(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    intersection = set_a.intersection(set_b)
    return list(intersection)
if __name__ == '__main__':
    list_a_sample = [1, 2, 3, 4, 5, 6]
    list_b_sample = [5, 6, 7, 8, 1, 9]
    result = find_intersection(list_a_sample, list_b_sample)
    print(result)