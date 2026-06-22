def find_middle(data):
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1], data[n // 2])
    else:
        return data[n // 2]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 3, 4, 5]
    list3 = [10, 20]
    list4 = [10, 20, 30]
    
    print(find_middle(list1))
    print(find_middle(list2))
    print(find_middle(list3))
    print(find_middle(list4))