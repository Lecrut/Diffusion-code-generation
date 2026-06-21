def temperature_difference(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    difference = abs(temp1 - temp2)
    
    if temp1 > temp2:
        magnitude = f"Temperature 1 ({temp1}) is greater than Temperature 2 ({temp2})"
    elif temp1 < temp2:
        magnitude = f"Temperature 2 ({temp2}) is greater than Temperature 1 ({temp1})"
    else:
        magnitude = "Both temperatures are equal"
    
    return difference, magnitude

if __name__ == '__main__':
    sample_temp1 = 40.5
    sample_temp2 = 35.8
    try:
        result = temperature_difference(sample_temp1, sample_temp2)
        print(f"Difference: {result[0]}")
        print(result[1])
    except ValueError as e:
        print(e)