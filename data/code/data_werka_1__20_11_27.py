def compare_items(a, b):
    if type(a) is type(b):
        return a == b
    return False
if __name__ == '__main__':
    sample1 = 42
    sample2 = 42.0
    sample3 = 'hello'
    sample4 = [1, 2, 3]
    print(compare_items(sample1, sample2))
    print(compare_items(sample3, sample3))
    print(compare_items(sample4, sample4))