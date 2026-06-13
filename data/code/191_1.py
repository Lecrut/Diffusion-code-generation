import itertools
def optimized_union(list_a, list_b):
    return list(set(list_a) | set(list_b))
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 2]
    list_b = [4, 5, 6, 7, 1]
    result = optimized_union(list_a, list_b)
    print(result)