def is_first_temp_greater(temp1, temp2):
    if not isinstance(temp1, int) or not isinstance(temp2, int):
        raise ValueError("Both temperatures must be integers.")
    return temp1 > temp2

if __name__ == '__main__':
    sample_temperature_one = 40
    sample_temperature_two = 35
    comparison_result = is_first_temp_greater(sample_temperature_one, sample_temperature_two)
    print(comparison_result)