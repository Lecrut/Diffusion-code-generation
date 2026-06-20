MIDDLE_INDEX = lambda n: n // 2

def find_middle(data):
    n = len(data)
    if n == 0:
        return None
    elif n % 2 == 1:
        middle_index = MIDDLE_INDEX(n)
        return data[middle_index]
    else:
        left_index = MIDDLE_INDEX(n) - 1
        right_index = MIDDLE_INDEX(n)
        return (data[left_index], data[right_index])
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [50]
    list4 = []
    list5 = [1, 2, 3, 4]
    list6 = [100, 200]
    print(find_middle(list1))
    print(find_middle(list2))
    print(find_middle(list3))
    print(find_middle(list4))
    print(find_middle(list5))
    print(find_middle(list6))