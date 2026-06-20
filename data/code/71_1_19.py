def find_middle_element(data):
    n = len(data)
    middle_index = (n - 1) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_lists = {
        "list1": [1, 2, 3, 4, 5],
        "list2": [10, 20, 30, 40],
        "list3": [100],
        "list4": [5, 15, 25, 35]
    }

    for key, value in sample_lists.items():
        print(f"{key}: {find_middle_element(value)}")