def compare_temperatures(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Both temperatures must be either int or float.")
    
    if temp1 > temp2:
        return "First temperature is higher."
    elif temp1 < temp2:
        return "Second temperature is higher."
    else:
        return "Both temperatures are equal."

if __name__ == '__main__':
    sample_temp1 = 30.0
    sample_temp2 = 28.5
    try:
        result = compare_temperatures(sample_temp1, sample_temp2)
        print(result)
    except ValueError as e:
        print(e)