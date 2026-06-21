import statistics

def find_middle_value(data):
    return statistics.median(data)

if __name__ == '__main__':
    list1 = [1, 3, 2]
    print(f"Median of {list1}: {find_middle_value(list1)}")
    list2 = [1, 5, 3, 4, 2]
    print(f"Median of {list2}: {find_middle_value(list2)}")