def compute_temperature_difference(temp_a, temp_b):
    difference = abs(temp_a - temp_b)
    return difference

if __name__ == '__main__':
    sample_temperature1 = 72.3
    sample_temperature2 = 68.5
    result = compute_temperature_difference(sample_temperature1, sample_temperature2)
    print(result)