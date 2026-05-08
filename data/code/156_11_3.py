def calculate_average(data):
    if not data:
        return 0
    return sum(data) / len(data)
if __name__ == '__main__':
    list1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    list2 = [10, 20, 30]
    list3 = []
    list4 = [7.5, 12.5, 15.0]
    print(f"Average of {list1}: {calculate_average(list1)}")
    print(f"Average of {list2}: {calculate_average(list2)}")
    print(f"Average of {list3}: {calculate_average(list3)}")
    print(f"Average of {list4}: {calculate_average(list4)}")