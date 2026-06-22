def compare_first_two_elements(lst):
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [10, 5]
    result = compare_first_two_elements(sample_list)
    print(result)

    another_sample_list = [3, 8]
    result = compare_first_two_elements(another_sample_list)
    print(result)