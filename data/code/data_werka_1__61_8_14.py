def find_element_at_index(lst, index):
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_index = 3
    result = find_element_at_index(sample_list, target_index)
    print(result)