def are_equal(var1, var2):
    return type(var1) == type(var2) and var1 == var2
if __name__ == '__main__':
    sample1 = 42
    sample2 = 42
    sample3 = '42'
    sample4 = 42.0
    print(are_equal(sample1, sample2))
    print(are_equal(sample1, sample3))
    print(are_equal(sample1, sample4))