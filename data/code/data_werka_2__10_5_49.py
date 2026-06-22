def temperature_difference(temp1, temp2):
    difference = abs(temp1 - temp2)
    
    if temp1 > temp2:
        magnitude = "Temperature 1 is greater than Temperature 2"
    elif temp1 < temp2:
        magnitude = "Temperature 2 is greater than Temperature 1"
    else:
        magnitude = "Both temperatures are equal"
    
    return difference, magnitude

if __name__ == '__main__':
    sample_temp1 = 25
    sample_temp2 = 35
    diff, rel_mag = temperature_difference(sample_temp1, sample_temp2)
    print(f"Difference: {diff}")
    print(rel_mag)