def determine_larger(value1, value2):
    if value1 > value2:
        return value1
    else:
        return value2

if __name__ == '__main__':
    sample_value1 = 42.5
    sample_value2 = 37
    larger_value = determine_larger(sample_value1, sample_value2)
    print(larger_value)