TEMPERATURE_THRESHOLD = 0

def is_first_temp_greater(temp1, temp2):
    if not isinstance(temp1, int) or not isinstance(temp2, int):
        raise ValueError("Both temperatures must be integers.")
    return temp1 > temp2

if __name__ == '__main__':
    sample_temperature_high = 45
    sample_temperature_low = 30
    result = is_first_temp_greater(sample_temperature_high, sample_temperature_low)
    print(result)