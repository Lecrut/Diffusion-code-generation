def find_middle_value(sorted_list):
    return sorted_list[len(sorted_list) // 2]

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9, 11]
    print(find_middle_value(sample_list))