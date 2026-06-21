def reverse_list(arr):
    return arr[::-1]

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", data)
    reversed_data = reverse_list(data)
    print("Reversed list:", reversed_data)

    data2 = [10, 20, 30, 40, 50]
    print("Original list:", data2)
    reversed_data2 = reverse_list(data2)
    print("Reversed list:", reversed_data2)

    data3 = [1, 2, 1, 3, 5, 4]
    print("Original list:", data3)
    reversed_data3 = reverse_list(data3)
    print("Reversed list:", reversed_data3)