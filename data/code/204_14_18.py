def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_data[mid_index]
    else:
        return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2

if __name__ == '__main__':
    list1 = [3.5, 2.1, 4.8, 1.9, 5.6]
    list2 = [100.2, 200.4, 300.6, 400.8, 501.0]
    list3 = []
    list4 = [7.7]

    print(f"List: {list1}, Median Value: {find_median(list1)}")
    print(f"List: {list2}, Median Value: {find_median(list2)}")
    print(f"List: {list3}, Median Value: {find_median(list3)}")
    print(f"List: {list4}, Median Value: {find_median(list4)}")