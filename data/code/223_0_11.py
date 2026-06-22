def find_max_value(numbers):
    return max(numbers) if numbers else None
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_max_value(list1))
    list2 = [-10, -5, -20, -1]
    print(find_max_value(list2))
    list3 = [7]
    print(find_max_value(list3))
    list4 = []
    print(find_max_value(list4))