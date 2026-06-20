def are_equal(var1, var2):
    return var1 == var2
if __name__ == '__main__':
    print(are_equal(1, 1))
    print(are_equal(1, '1'))
    print(are_equal([1, 2], [1, 2]))
    print(are_equal([1, 2], (1, 2)))