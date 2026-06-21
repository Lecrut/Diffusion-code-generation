def find_median(data):
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Input must be a list of floats or integers.")
    
    n = len(data)
    if n == 0:
        return None
    
    sorted_data = sorted(data)
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
    list6 = [1, 2, 3, 4]
    
    print(f"List: {list1}, Median Value: {find_median(list1)}")
    print(f"List: {list2}, Median Value: {find_median(list2)}")
    print(f"List: {list3}, Median Value: {find_median(list3)}")
    print(f"List: {list4}, Median Value: {find_median(list4)}")
    print(f"List: {list5}, Median Value: {find_median(list5)}")
    print(f"List: {list6}, Median Value: {find_median(list6)}")