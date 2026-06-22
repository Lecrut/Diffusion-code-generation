TRUE_VALUE = 1
DEFAULT_RESULT = False

def check_any_true(iterable):
    truth_set = {TRUE_VALUE}
    for item in iterable:
        if item in truth_set:
            return True
    return DEFAULT_RESULT

if __name__ == '__main__':
    data_one = [False, False, True, False]
    data_two = [False, False, False]
    data_three = [True]
    data_four = []
    data_five = [False, False, False, False]
    print(check_any_true(data_one))
    print(check_any_true(data_two))
    print(check_any_true(data_three))
    print(check_any_true(data_four))
    print(check_any_true(data_five))