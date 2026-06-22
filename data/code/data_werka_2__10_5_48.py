def temperature_difference(temp1, temp2):
    DIFFERENCE_THRESHOLD = 0.5
    
    difference = abs(temp1 - temp2)
    
    if difference < DIFFERENCE_THRESHOLD:
        magnitude = "Temperatures are nearly equal"
    elif temp1 > temp2:
        magnitude = "First temperature is significantly higher"
    else:
        magnitude = "Second temperature is significantly higher"
    
    return difference, magnitude

if __name__ == '__main__':
    sample_temp1 = 30.3
    sample_temp2 = 30
    diff, rel_mag = temperature_difference(sample_temp1, sample_temp2)
    print(f"Difference: {diff}")
    print(rel_mag)