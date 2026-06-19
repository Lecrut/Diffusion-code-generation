def are_sums_different(list1, list2):
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 15, 25, 20]
    result = are_sums_different(list_a, list_b)
    print(result)