def find_middle_value(data):
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        upper_middle_index = n // 2
        lower_middle_index = upper_middle_index - 1
        median = (data[lower_middle_index] + data[upper_middle_index]) / 2
        return median

if __name__ == '__main__':
    list1 = [5, 3, 7, 1, 2]
    print(f"Median of {list1}: {find_middle_value(list1)}")