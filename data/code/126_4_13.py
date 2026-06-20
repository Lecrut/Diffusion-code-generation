def check_equality(a, b):
    if type(a) != type(b):
        return False
    return a == b

if __name__ == '__main__':
    sample_a = 3.14
    sample_b = 3.14
    result = check_equality(sample_a, sample_b)
    print("Sample Test Case (Floats):", result)

    sample_c = "Python"
    sample_d = "Java"
    result = check_equality(sample_c, sample_d)
    print("Sample Test Case (Strings):", result)

    sample_e = [1, 2, 3]
    sample_f = [1, 2, 4]
    result = check_equality(sample_e, sample_f)
    print("Sample Test Case (Lists):", result)