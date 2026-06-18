import sys

def parse_temperature(value):
    """Parse a string to float temperature value."""
    return float(value)

def compare_temp(temp_a, temp_b):
    """Compare two temperatures and return a formatted result."""
    if temp_a == temp_b:
        print(f"{temp_a} is equal to {temp_b}")
    elif temp_a > temp_b:
        print(f"{temp_a} is higher than {temp_b}")
    else:
        print(f"{temp_a} is lower than {temp_b}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input calls)
    temperature_1 = parse_temperature(25.5)
    temperature_2 = parse_temperature(30.0)

    compare_temp(temperature_1, temperature_2)