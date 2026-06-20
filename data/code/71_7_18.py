MIDDLE_INDEX_EVEN = 1

def find_middle_element(data):
    n = len(data)
    if n == 0:
        return None
    middle_index = (n - MIDDLE_INDEX_EVEN) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list_odd = [1, 5, 2, 8, 3]
    result_odd = find_middle_element(sample_list_odd)
    print(result_odd)

    sample_list_even = [10, 20, 30, 40, 50, 60]
    result_even = find_middle_element(sample_list_even)
    print(result_even)