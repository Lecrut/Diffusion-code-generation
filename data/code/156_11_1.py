def calculate_average(data):
    if not data:
        return 0
    return sum(data) / len(data)
if __name__ == '__main__':
    list1 = [1.0, 2.5, 3.5]
    list2 = [10, 20, 30, 40]
    list3 = []
    list4 = [5]
    list5 = [-1, 1, 3]
    print(f"Average of {list1}: {calculate_average(list1)}")
    print(f"Average of {list2}: {calculate_average(list2)}")
    print(f"Average of {list3}: {calculate_average(list3)}")
    print(f"Average of {list4}: {calculate_average(list4)}")
    print(f"Average of {list5}: {calculate_average(list5)}")