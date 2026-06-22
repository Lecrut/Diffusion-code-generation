def check_inequality(value1, value2):
    if type(value1) is not type(value2):
        return True
    return value1 != value2

if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = "42"
    print(check_inequality(sample_value1, sample_value2))