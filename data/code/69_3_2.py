def reverse_list_indices(data):
    n = len(data)
    for i in range(n // 2):
        j = n - 1 - i
        data[i], data[j] = data[j], data[i]
    return data
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list_indices(sample_list)
    print(reversed_list)