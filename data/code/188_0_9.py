def reverse_list(lst):
    return lst[::-1]

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7]
    print("Reversed list:", reverse_list(data))
    data2 = [10, 20, 30, 40, 50]
    print("Reversed list:", reverse_list(data2))
    data3 = [1, 2, 1, 3, 5, 4]
    print("Reversed list:", reverse_list(data3))