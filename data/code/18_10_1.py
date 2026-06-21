def get_middle_element(lst):
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50]
    sample_even = [100, 200, 300, 400]
    result_odd = get_middle_element(sample_odd)
    result_even = get_middle_element(sample_even)
    print(result_odd)
    print(result_even)