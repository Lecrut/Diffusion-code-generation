MIDDLE_INDEX = lambda n: n // 2

def find_middle(data):
    n = len(data)
    if n == 0:
        return None
    elif n % 2 == 1:
        middle_index = MIDDLE_INDEX(n)
        return data[middle_index]
    else:
        middle_index_1 = MIDDLE_INDEX(n) - 1
        middle_index_2 = MIDDLE_INDEX(n)
        return (data[middle_index_1], data[middle_index_2])

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [50]
    list4 = []
    list5 = [1, 2, 3, 4]
    list6 = [100, 200]

    for lst in (list1, list2, list3, list4, list5, list6):
        print(find_middle(lst))