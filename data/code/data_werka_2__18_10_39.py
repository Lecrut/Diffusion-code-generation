def compare_first_second(lst):
    first_element = lst[0]
    second_element = lst[1]
    return first_element > second_element

if __name__ == '__main__':
    sample_list = [42, 35]
    result = compare_first_second(sample_list)
    print(result)

    another_sample_list = [8.5, 9.2]
    another_result = compare_first_second(another_sample_list)
    print(another_result)