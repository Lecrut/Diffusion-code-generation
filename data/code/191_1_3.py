def union_optimized(list_a, list_b):
    return list(set(list_a) | set(list_b))
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = union_optimized(list_a, list_b)
    print(result)