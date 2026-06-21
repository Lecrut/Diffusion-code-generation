def validate_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Temperature must be a number")

def compare_temperatures(temp1, temp2):
    validate_temperature(temp1)
    validate_temperature(temp2)
    DIFFERENCE_THRESHOLD = 0.01
    difference = abs(temp1 - temp2)
    
    if difference < DIFFERENCE_THRESHOLD:
        yield "Both temperatures are essentially equal"
    elif temp1 > temp2:
        yield f"T1 is warmer by {difference:.2f} degrees"
    else:
        yield f"T2 is warmer by {difference:.2f} degrees"

if __name__ == '__main__':
    for result in compare_temperatures(30.5, 25.3):
        print(result)
    for result in compare_temperatures(28.7, 35.1):
        print(result)
    for result in compare_temperatures(20.0, 20.0):
        print(result)