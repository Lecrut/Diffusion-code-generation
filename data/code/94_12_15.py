def has_truthy_value(items):
    return any(items)
if __name__ == '__main__':
    sample1 = [0, 0, 0]
    sample2 = [0, 1, 0]
    sample3 = []
    sample4 = [None, False, 0]
    sample5 = [None, False, 1]
    print(has_truthy_value(sample1))
    print(has_truthy_value(sample2))
    print(has_truthy_value(sample3))
    print(has_truthy_value(sample4))
    print(has_truthy_value(sample5))