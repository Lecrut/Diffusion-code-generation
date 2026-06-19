def verify_equality(var1, var2):
    return type(var1) == type(var2) and var1 == var2
if __name__ == '__main__':
    sample1 = 42
    sample2 = 42.0
    sample3 = '42'
    sample4 = [1, 2, 3]
    sample5 = [1, 2, 3]
    print(verify_equality(sample1, sample2))
    print(verify_equality(sample1, sample1))
    print(verify_equality(sample3, sample4))
    print(verify_equality(sample4, sample5))