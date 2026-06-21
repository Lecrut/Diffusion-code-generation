def find_median(data):
    if not data:
        raise ValueError("Input list is empty")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    middle_index = n // 2
    
    if n % 2 == 1:
        return sorted_data[middle_index]
    else:
        return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [5.5, 6.6, 7.7]
    list4 = [100]
    list5 = []
    
    try:
        print(f"List: {list1}, Median Value: {find_median(list1)}")
        print(f"List: {list2}, Median Value: {find_median(list2)}")
        print(f"List: {list3}, Median Value: {find_median(list3)}")
        print(f"List: {list4}, Median Value: {find_median(list4)}")
        print(f"List: {list5}, Median Value: {find_median(list5)}")
    except ValueError as e:
        print(e)