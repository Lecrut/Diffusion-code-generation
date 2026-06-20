def compare_values(a, b):
    return a == b
if __name__ == '__main__':
    print(compare_values(1, 1))
    print(compare_values(1, '1'))
    print(compare_values([1, 2], [1, 2]))
    print(compare_values([1, 2], (1, 2)))