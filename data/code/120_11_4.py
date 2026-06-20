def compare_values(a, b):
    return a == b
if __name__ == '__main__':
    result = compare_values(5, 5)
    print(result)
    result = compare_values(5, '5')
    print(result)
    result = compare_values([1, 2], [1, 2])
    print(result)
    result = compare_values([1, 2], (1, 2))
    print(result)