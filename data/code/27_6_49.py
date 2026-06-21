def are_sums_different(list1, list2):
    return sum(list1) != sum(list2)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [5, 4, 3, 2, 1]
    print(are_sums_different(list_a, list_b))