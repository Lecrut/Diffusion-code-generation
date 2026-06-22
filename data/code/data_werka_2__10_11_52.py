def validate_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Temperature must be an integer or float")

def temperature_difference(temp1, temp2):
    validate_temperature(temp1)
    validate_temperature(temp2)
    return abs(temp1 - temp2)

if __name__ == '__main__':
    sample_temp1 = 75.0
    sample_temp2 = 68.4
    result = temperature_difference(sample_temp1, sample_temp2)
    print(result)