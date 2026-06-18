import sys

def calculate_mean(temp1: float, temp2: float) -> str:
    """Calculate the arithmetic mean of two temperature readings formatted to two decimal places."""
    average = (temp1 + temp2) / 2
    return f"{average:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user input or command-line arguments used.
    reading_a = 365.0
    reading_b = -1984.0
    
    result = calculate_mean(reading_a, reading_b)
    
    print(result)