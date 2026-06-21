def compare_temperatures(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Both temperatures must be numbers.")
    
    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        yield f"T1 is warmer by {difference} degrees"
    elif temp1 < temp2:
        yield f"T2 is warmer by {difference} degrees"
    else:
        yield "Both temperatures are equal"

if __name__ == '__main__':
    for result in compare_temperatures(30, 25):
        print(result)