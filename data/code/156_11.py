def calculate_average(data):
    if not data:
        return 0
    return sum(data) / len(data)
if __name__ == '__main__':
    list1 = [1.0, 2.5, 3.5, 4.0]
    list2 = [10, 20, 30, 40, 50]
    list3 = []
    list4 = [7.0]
    print(calculate_average(list1))
    print(calculate_average(list2))
    print(calculate_average(list3))
    print(calculate_average(list4))