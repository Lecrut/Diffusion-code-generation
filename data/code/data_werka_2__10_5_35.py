def compare_temperatures(temp1, temp2):
    difference = abs(temp1 - temp2)
    
    if temp1 > temp2:
        relative_magnitude = "temp1 is greater than temp2"
    elif temp1 < temp2:
        relative_magnitude = "temp1 is less than temp2"
    else:
        relative_magnitude = "temp1 is equal to temp2"
    
    return difference, relative_magnitude

if __name__ == '__main__':
    sample_temp1 = 30.5
    sample_temp2 = 25.0
    
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)