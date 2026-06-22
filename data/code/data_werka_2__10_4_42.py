def validate_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Temperature must be a number")

def compare_temperatures(temp1, temp2):
    validate_temperature(temp1)
    validate_temperature(temp2)
    
    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        yield f"T1 is warmer by {difference} degrees"
    elif temp2 > temp1:
        yield f"T2 is warmer by {difference} degrees"
    else:
        yield "Both temperatures are equal"

if __name__ == '__main__':
    for result in compare_temperatures(30, 25):
        print(result)
    for result in compare_temperatures(28, 35):
        print(result)
    for result in compare_temperatures(20, 20):
        print(result)