def values_differ(a, b):
    return not a == b
if __name__ == '__main__':
    sample1 = [1, 2, 3]
    sample2 = (1, 2, 3)
    sample3 = {'key': 'value'}
    sample4 = {'key': 'value'}
    sample5 = 42
    sample6 = 42.0
    print(values_differ(sample1, sample2))
    print(values_differ(sample3, sample4))
    print(values_differ(sample5, sample6))