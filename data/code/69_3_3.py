def reverse_list_indices(data):
    n = len(data)
    for i in range(n // 2):
        j = i
        while j < n - 1 - i:
            data[j], data[j + 1] = data[j + 1], data[j]
            j += 1
    return data
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", sample_list)
    reversed_list = reverse_list_indices(sample_list)
    print("Reversed list:", reversed_list)