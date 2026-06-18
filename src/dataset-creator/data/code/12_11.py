def simple_arithmetic(a, b):
    sum_val = a + b
    diff_val = a - b
    return (sum_val, diff_val)
if __name__ == '__main__':
    result = simple_arithmetic(10, 4)
    print(result)