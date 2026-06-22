TRUTHY_CHECKER = lambda lst: any(lst)

if __name__ == '__main__':
    SAMPLE_LIST1 = [0, False, None, '']
    SAMPLE_LIST2 = [0, False, None, 'hello']
    print(TRUTHY_CHECKER(SAMPLE_LIST1))
    print(TRUTHY_CHECKER(SAMPLE_LIST2))