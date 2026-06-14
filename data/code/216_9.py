def calculate_middle(data):
    n = len(data)
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    sorted_list = [1, 5, 8, 12, 15]
    middle_value = calculate_middle(sorted_list)
    print(middle_value)