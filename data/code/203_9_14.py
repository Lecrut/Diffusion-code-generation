def are_close(num1, num2, tolerance=1e-9):
    return abs(num1 - num2) <= tolerance

if __name__ == '__main__':
    sample_num1 = 0.30000000001
    sample_num2 = 0.30000000002
    result = are_close(sample_num1, sample_num2)
    print(result)