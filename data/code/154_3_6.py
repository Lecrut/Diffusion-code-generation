TARGET_VALUE = 3

def count_target_value(lst):
    return lst.count(TARGET_VALUE)

if __name__ == '__main__':
    sample_list = [1, 2, TARGET_VALUE, 4, 5, TARGET_VALUE, 7]
    result = count_target_value(sample_list)
    print(result)