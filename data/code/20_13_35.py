def verify_equality(var1, var2):
    return type(var1) == type(var2) and var1 == var2
if __name__ == '__main__':
    sample_var1 = 42
    sample_var2 = 42
    sample_var3 = '42'
    print(verify_equality(sample_var1, sample_var2))
    print(verify_equality(sample_var1, sample_var3))