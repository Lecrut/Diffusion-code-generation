def find_middle_element(lst):
    index = len(lst) // 2
    return lst[index]

if __name__ == '__main__':
    sample_list = [1.5, 2.3, 3.7, 4.1, 5.9]
    print(find_middle_element(sample_list))