def float_exists(float_list, target):
    return any(abs(num - target) < 1e-9 for num in float_list)

if __name__ == '__main__':
    sample_list = [3.141592653589793, 2.718281828459045, 1.414213562373095]
    target_value = 3.14
    print(float_exists(sample_list, target_value))