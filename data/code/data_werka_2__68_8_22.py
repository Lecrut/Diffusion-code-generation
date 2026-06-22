def find_first_zero_difference_index(list_a, list_b):
    min_length = min(len(list_a), len(list_b))
    for i in range(min_length - 1):
        if list_a[i] == list_b[i + 1]:
            return i
    return -1

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [0, 1, 2, 3, 6]
    index = find_first_zero_difference_index(list_a, list_b)
    print(index)