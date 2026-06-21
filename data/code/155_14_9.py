def sum_floats(float_list):
    TOTAL = 0.0
    for value in float_list:
        TOTAL += value
    return TOTAL

if __name__ == '__main__':
    SAMPLE_VALUES = [1.5, 2.5, 3.5]
    result = sum_floats(SAMPLE_VALUES)
    print(result)