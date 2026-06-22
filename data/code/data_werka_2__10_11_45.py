def calculate_difference(temp_a, temp_b):
    difference = abs(temp_a - temp_b)
    return difference

if __name__ == '__main__':
    sample_temperature1 = 28.4
    sample_temperature2 = 35.6
    result = calculate_difference(sample_temperature1, sample_temperature2)
    print(result)