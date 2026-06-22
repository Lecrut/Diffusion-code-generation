def validate_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Temperature must be an integer or float")

def temperature_difference(temp1, temp2):
    validate_temperature(temp1)
    validate_temperature(temp2)
    
    difference = abs(temp1 - temp2)
    
    if temp1 > temp2:
        magnitude = "First temperature is greater than the second"
    elif temp1 < temp2:
        magnitude = "Second temperature is greater than the first"
    else:
        magnitude = "Both temperatures are equal"
    
    return difference, magnitude

if __name__ == '__main__':
    sample_temp1 = 40
    sample_temp2 = 25
    diff, rel_mag = temperature_difference(sample_temp1, sample_temp2)
    print(f"Difference: {diff}")
    print(rel_mag)