def find_middle_element(data):
    sorted_data = sorted(data)
    middle_index = len(sorted_data) // 2
    return sorted_data[middle_index]

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5]
    print(f"List: {sample_list1}, Middle Element: {find_middle_element(sample_list1)}")
    sample_list2 = [7, 9, 6, 8, 2]
    print(f"List: {sample_list2}, Middle Element: {find_middle_element(sample_list2)}")