TARGET_VALUE = 5

def check_any_match(data):
    return any((item == TARGET_VALUE for item in data))
if __name__ == '__main__':
    sample_list = [1, 5, 2, 5, 8, 5, 3]
    result = check_any_match(sample_list)
    print(result)
    sample_list_2 = [10, 20, 10, 30, 10]
    result_2 = check_any_match(sample_list_2)
    print(result_2)
    sample_list_3 = [1, 2, 3, 4, 5]
    result_3 = check_any_match(sample_list_3)
    print(result_3)