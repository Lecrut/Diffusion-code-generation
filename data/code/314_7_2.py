def calculate_list_sum(data):
    total = 0
    for item in data:
        total += item
    return total
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(calculate_list_sum(list1))
    list2 = [10, -5, 20, 0]
    print(calculate_list_sum(list2))
    list3 = []
    print(calculate_list_sum(list3))
    list4 = [1.5, 2.5, 3.0]
    print(calculate_list_sum(list4))