def compare_temperatures(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Temperatures must be numbers")
    
    DIFFERENCE_THRESHOLD = 0.0
    
    difference = abs(temp1 - temp2)
    if difference < DIFFERENCE_THRESHOLD:
        yield "Both temperatures are equal"
    elif temp1 > temp2:
        yield f"T1 is warmer by {difference} degrees"
    else:
        yield f"T2 is warmer by {difference} degrees"

if __name__ == '__main__':
    for result in compare_temperatures(30, 25):
        print(result)
    for result in compare_temperatures(20, 20):
        print(result)
    for result in compare_temperatures(15, 22):
        print(result)