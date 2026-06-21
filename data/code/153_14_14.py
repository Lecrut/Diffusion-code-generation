TARGET_VALUE = 42

def find_target_exists(data):
    return TARGET_VALUE in data
if __name__ == '__main__':
    sample_list = [10, 25, 3, 42, 8, 25, 99]
    result1 = find_target_exists(sample_list)
    print(f'List: {sample_list}, Target Exists: {result1}')
    sample_list_2 = [1, 5, 9, 12, 15]
    result2 = find_target_exists(sample_list_2)
    print(f'List: {sample_list_2}, Target Exists: {result2}')
    sample_list_3 = [5, 10, 15, 20]
    result3 = find_target_exists(sample_list_3)
    print(f'List: {sample_list_3}, Target Exists: {result3}')