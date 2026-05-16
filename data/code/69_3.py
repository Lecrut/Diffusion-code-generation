def reverse_list_indices(data):
    n = len(data)
    for i in range(n // 2):
        j = i + 1
        temp = data[i]
        data[i] = data[j]
        data[j] = temp
    return data
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(sample_list)
    reversed_list = reverse_list_indices(sample_list)
    print(reversed_list)
    sample_list_2 = [10, 20, 30, 40, 50, 60]
    print(sample_list_2)
    reversed_list_2 = reverse_list_indices(sample_list_2)
    print(reversed_list_2)
    sample_list_3 = [1, 2, 3, 4]
    print(sample_list_3)
    reversed_list_3 = reverse_list_indices(sample_list_3)
    print(reversed_list_3)