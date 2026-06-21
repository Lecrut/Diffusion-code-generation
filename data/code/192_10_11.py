def find_common_elements(*lists):
    return sorted(set.intersection(*map(set, lists)))

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 5]
    list_b = [4, 5, 6, 7, 8, 4]
    result = find_common_elements(list_a, list_b)
    print(result)