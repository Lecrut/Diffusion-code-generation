def determine_larger(value1, value2):
    return value1 if value1 > value2 else value2

if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 3.14
    larger_value = determine_larger(sample_value1, sample_value2)
    print(larger_value)