def calculate_symmetric_difference(set1, set2):
    return set1 ^ set2
if __name__ == '__main__':
    first_set = {10, 20, 30, 40}
    second_set = {30, 40, 50, 60}
    result = calculate_symmetric_difference(first_set, second_set)
    print('Symmetric Difference:', result)