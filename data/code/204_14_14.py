def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    middle_index = n // 2
    if n % 2 == 1:
        return sorted_data[middle_index]
    else:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2.0

if __name__ == '__main__':
    list1 = [3.5, 1.2, 4.8, 2.9, 5.6]
    list2 = [100.1, 200.2, 300.3]
    list3 = []
    list4 = [7.7]

    print(f"List: {list1}, Median Value: {find_median(list1)}")
    print(f"List: {list2}, Median Value: {find_median(list2)}")
    print(f"List: {list3}, Median Value: {find_median(list3)}")
    print(f"List: {list4}, Median Value: {find_median(list4)}")