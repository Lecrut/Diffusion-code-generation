def get_middle_element(data):
    if not data:
        raise ValueError("List cannot be empty")
    index = len(data) // 2
    return data[index]

if __name__ == '__main__':
    sample_lists = [[1, 2, 3, 4, 5], [10, 20, 30], ['a', 'b', 'c', 'd'], [True, False, True, False, True]]
    for lst in sample_lists:
        result = get_middle_element(lst)
        print(result)