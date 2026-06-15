def find_first_occurrence(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1
if __name__ == '__main__':
    my_list = [10, 25, 30, 45, 25, 50]
    target_value = 25
    index = find_first_occurrence(my_list, target_value)
    print(index)