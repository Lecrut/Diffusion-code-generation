def validate_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Temperature must be an integer or float")

def compare_temperatures(temp1, temp2):
    validate_temperature(temp1)
    validate_temperature(temp2)
    return temp1 if temp1 > temp2 else temp2

if __name__ == '__main__':
    sample_temp1 = 15.0
    sample_temp2 = 20.3
    higher_temperature = compare_temperatures(sample_temp1, sample_temp2)
    print(higher_temperature)