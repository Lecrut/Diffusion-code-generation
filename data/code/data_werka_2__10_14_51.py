def validate_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Temperature must be a number")

def compare_temperatures(temp1, temp2):
    validate_temperature(temp1)
    validate_temperature(temp2)
    
    return temp1 if temp1 > temp2 else temp2

if __name__ == '__main__':
    sample_temp1 = 45.0
    sample_temp2 = 50.3
    higher_temperature = compare_temperatures(sample_temp1, sample_temp2)
    print(higher_temperature)