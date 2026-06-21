def temperature_difference(temp1, temp2):
    difference = abs(temp1 - temp2)
    
    if temp1 > temp2:
        magnitude = "First temperature is greater than second"
    elif temp1 < temp2:
        magnitude = "Second temperature is greater than first"
    else:
        magnitude = "Both temperatures are equal"
    
    return difference, magnitude

if __name__ == '__main__':
    sample_temp1 = 25
    sample_temp2 = 30
    diff, rel_mag = temperature_difference(sample_temp1, sample_temp2)
    print(f"Difference: {diff}")
    print(rel_mag)