def sum_floats(float_list):
    total = 0.0
    for value in float_list:
        total += value
    return total

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    result = sum_floats(sample_values)
    print(result)