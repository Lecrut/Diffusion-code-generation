def compare_first_and_sixth(lst):
    if len(lst) < 6:
        raise ValueError("List must have at least 6 elements")
    return lst[0] > lst[5]

if __name__ == '__main__':
    test_list = [100, 20, 30, 40, 50, 10]
    print(compare_first_and_sixth(test_list))