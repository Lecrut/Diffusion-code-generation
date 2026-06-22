TRUE_SENTINEL = True
FALSE_SENTINEL = False

def check_truth_presence(bool_list):
    if not bool_list:
        return FALSE_SENTINEL
    for element in bool_list:
        if element is TRUE_SENTINEL:
            return TRUE_SENTINEL
    return FALSE_SENTINEL

if __name__ == '__main__':
    test_set = [FALSE_SENTINEL, FALSE_SENTINEL, TRUE_SENTINEL, FALSE_SENTINEL]
    found = check_truth_presence(test_set)
    print(found)