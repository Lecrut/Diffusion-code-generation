def values_differ(a, b):
    return a != b

if __name__ == '__main__':
    value1 = 42
    value2 = '42'
    print(values_differ(value1, value2))