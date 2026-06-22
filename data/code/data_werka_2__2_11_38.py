def validate_input(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be a number")

def liters_to_gallons(liters):
    validate_input(liters)
    conversion_rate = 0.264172
    return liters * conversion_rate

if __name__ == '__main__':
    sample_values = [5.0, 15.0, 30.0, 45.0]
    for value in sample_values:
        print(f"{value} liters is {liters_to_gallons(value)} gallons")