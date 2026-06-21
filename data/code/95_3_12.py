LOWER_BOUND = 0
UPPER_BOUND = 100

def is_valid_candidate(value):
    return value > LOWER_BOUND and value < UPPER_BOUND and value % 2 == 0

if __name__ == '__main__':
    test_num = 42
    result = is_valid_candidate(test_num)
    print(result)
    test_num = 99
    result = is_valid_candidate(test_num)
    print(result)
    test_num = -10
    result = is_valid_candidate(test_num)
    print(result)