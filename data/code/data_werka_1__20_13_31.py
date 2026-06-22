def verify_equality(var1, var2):
    return isinstance(var1, type(var2)) and var1 == var2
if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 42
    sample_value3 = '42'
    print(verify_equality(sample_value1, sample_value2))
    print(verify_equality(sample_value1, sample_value3))