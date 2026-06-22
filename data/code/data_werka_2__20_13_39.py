def verify_equality(var1, var2):
    if type(var1) != type(var2):
        return False
    return var1 == var2
if __name__ == '__main__':
    sample1 = 42
    sample2 = 42.0
    sample3 = 'hello'
    sample4 = 'hello'
    print(verify_equality(sample1, sample2))
    print(verify_equality(sample3, sample4))