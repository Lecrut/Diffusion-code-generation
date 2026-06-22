def calculate_temp_difference(temp_a, temp_b):
    return abs(temp_a - temp_b)

if __name__ == '__main__':
    sample_temp_a = 35.0
    sample_temp_b = 40.2
    result = calculate_temp_difference(sample_temp_a, sample_temp_b)
    print(result)