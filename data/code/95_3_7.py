def check_value(value):
    return value > 0 and value % 2 == 0 and value < 100

if __name__ == '__main__':
    sample_values = [0, 2, 50, 100, -5]
    results = [check_value(v) for v in sample_values]
    print(results)