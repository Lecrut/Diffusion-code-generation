check_greater = lambda l: (l[0] > l[1]) if len(l) >= 2 else False
if __name__ == '__main__':
    test_list = [8, 6]
    print(check_greater(test_list))