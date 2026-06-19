def values_differ(a, b):
    return a != b

if __name__ == '__main__':
    sample1 = 42
    sample2 = '42'
    result = values_differ(sample1, sample2)
    print(result)