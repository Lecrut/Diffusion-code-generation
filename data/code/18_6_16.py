def find_middle(lst):
    return lst[len(lst) // 2]

if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    data2 = [10, 20, 30, 40, 50, 60]
    data3 = [99]
    data4 = [1, 2]

    print(find_middle(data1))
    print(find_middle(data2))
    print(find_middle(data3))
    print(find_middle(data4))