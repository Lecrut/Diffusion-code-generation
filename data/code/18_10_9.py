def get_middle_element(lst):
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_odd = [1, 3, 5, 7, 9]
    sample_even = [2, 4, 6, 8]
    print(get_middle_element(sample_odd))
    print(get_middle_element(sample_even))