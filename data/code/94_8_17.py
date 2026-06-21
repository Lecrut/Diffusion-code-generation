TRUE_STATE = {True: True}

def detect_truth(values):
    if not values:
        return False
    for v in values:
        if v in TRUE_STATE:
            return True
    return False

if __name__ == '__main__':
    test_list = [False, False, True, False]
    print(detect_truth(test_list))