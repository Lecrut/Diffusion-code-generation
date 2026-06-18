import sys

def calculate_mean(temp1: float, temp2: float) -> str:
    """
    Calculates the arithmetic mean of two temperature readings
    and returns it formatted to two decimal places.
    
    Args:
        temp1 (float): The first temperature reading in Celsius or Fahrenheit.
        temp2 (float): The second temperature reading in Celsius or Fahrenheit.
        
    Returns:
        str: The average value as a string with exactly two digits after the dot.
    """
    mean_value = (temp1 + temp2) / 2
    return f"{mean_value:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes without user input
    reading_a: float = 23.5
    reading_b: float = 24.1
    
    average_temp: str = calculate_mean(reading_a, reading_b)
    
    print(f"The arithmetic mean of {reading_a} and {reading_b} is {average_temp}")