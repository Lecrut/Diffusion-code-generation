def calculate_symmetric_difference(set1, set2):
    return set1 ^ set2

if __name__ == '__main__':
    first_set = {7, 8, 9, 10}
    second_set = {9, 10, 11, 12}
    symmetric_diff_result = calculate_symmetric_difference(first_set, second_set)
    print("Symmetric difference between first_set and second_set:", symmetric_diff_result)

    third_set = {'x', 'y', 'z'}
    fourth_set = {'w', 'x', 'z'}
    symmetric_diff_result_2 = calculate_symmetric_difference(third_set, fourth_set)
    print("Symmetric difference between third_set and fourth_set:", symmetric_diff_result_2)