def reverse_list(arr):
    return arr[::-1]

if __name__ == '__main__':
    data = [8, 7, 6, 5, 4, 3, 2, 1]
    print("Original list:", data)
    reversed_data = reverse_list(data)
    print("Reversed list:", reversed_data)

    data2 = [10, 20, 30, 40, 50, 60]
    print("Original list:", data2)
    reversed_data2 = reverse_list(data2)
    print("Reversed list:", reversed_data2)

    data3 = [1, 2, 3, 3, 2, 1]
    print("Original list:", data3)
    reversed_data3 = reverse_list(data3)
    print("Reversed list:", reversed_data3)