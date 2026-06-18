import math

def calculate_temperature_mean(temp1: float, temp2: float) -> str:
    """Calculate the arithmetic mean of two temperature readings formatted to two decimal places."""
    average = (temp1 + temp2) / 2
    return f"{average:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements, no user input or external dependencies needed.
    reading_a: float = 75.0
    reading_b: float = 83.5
    
    mean_result: str = calculate_temperature_mean(reading_a, reading_b)
    
    print(f"The arithmetic mean of {reading_a} and {reading_b} is {mean_result}")