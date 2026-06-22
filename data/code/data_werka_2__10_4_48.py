def compare_temperatures(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Temperatures must be numbers")
    
    difference = abs(temp1 - temp2)
    
    if temp1 > temp2:
        return f"T1 is warmer by {difference} degrees"
    elif temp2 > temp1:
        return f"T2 is warmer by {difference} degrees"
    else:
        return "Both temperatures are equal"

if __name__ == '__main__':
    sample_temps = [(40, 35), (28, 30), (25, 25)]
    
    for temp1, temp2 in sample_temps:
        result = compare_temperatures(temp1, temp2)
        print(result)