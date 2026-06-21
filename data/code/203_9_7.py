def are_close(num1, num2, tolerance=1e-9):
    return abs(num1 - num2) <= tolerance

if __name__ == '__main__':
    sample_num1 = 0.5 + 0.4
    sample_num2 = 0.9
    result = are_close(sample_num1, sample_num2)
    print(result)