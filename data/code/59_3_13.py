def find_middle_element(data):
    return sorted(data)[len(data) // 2]

if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5]
    print(find_middle_element(sample1))
    sample2 = [9, 2, 6, 5, 3, 5]
    print(find_middle_element(sample2))