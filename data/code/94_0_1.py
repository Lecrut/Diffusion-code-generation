import sys
def check_at_least_one_true(bool_list):
    for value in bool_list:
        if value:
            return True
    return False
if __name__ == '__main__':
    sample_list = [False, False, True, False, False]
    result = check_at_least_one_true(sample_list)
    print(result)