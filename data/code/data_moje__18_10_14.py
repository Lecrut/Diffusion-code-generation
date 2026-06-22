def get_middle_element(lst):
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [10, 20, 30, 40]
    print(get_middle_element(sample_odd))
    print(get_middle_element(sample_even))