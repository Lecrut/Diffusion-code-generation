def compare_temperatures(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Both inputs must be integers or floats.")
    
    if temp1 > temp2:
        return "First temperature is higher."
    elif temp1 < temp2:
        return "Second temperature is higher."
    else:
        return "Both temperatures are equal."

if __name__ == '__main__':
    sample_temp1 = 30.5
    sample_temp2 = 28.9
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)