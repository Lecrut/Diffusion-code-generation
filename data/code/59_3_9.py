def find_middle_element(data):
    return sorted(data)[len(data) // 2]

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5]
    print(find_middle_element(sample_list))