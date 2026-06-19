def find_first_zero_difference_index(list_a, list_b):
    for i in range(len(list_a) - 1):
        if list_a[i] - list_b[i + 1] == 0:
            return i
    return -1

if __name__ == '__main__':
    list_a = [5, 3, 8, 6, 7]
    list_b = [2, 3, 6, 9, 7]
    index = find_first_zero_difference_index(list_a, list_b)
    print(index)