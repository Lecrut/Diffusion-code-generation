def find_middle(data):
    n = len(data)
    if n == 0:
        return None
    if n % 2 == 1:
        return data[n // 2]
    else:
        middle1 = data[n // 2 - 1]
        middle2 = data[n // 2]
        return (middle1 + middle2) // 2
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    print(find_middle(list1))
    list2 = [10, 20, 30, 40, 50, 60]
    print(find_middle(list2))
    list3 = [7]
    print(find_middle(list3))
    list4 = []
    print(find_middle(list4))