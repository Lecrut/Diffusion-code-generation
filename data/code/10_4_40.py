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
    print(compare_temperatures(30, 25))
    print(compare_temperatures(28, 35))
    print(compare_temperatures(20, 20))
    print(compare_temperatures(15, 22))