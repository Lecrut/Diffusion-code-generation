def compare_values(a, b):
    return a == b

if __name__ == '__main__':
    print(compare_values(5, 5))
    print(compare_values(5, "5"))
    print(compare_values([1, 2], [1, 2]))
    print(compare_values([1, 2], [2, 1]))