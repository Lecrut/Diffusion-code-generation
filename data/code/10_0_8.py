temperature_a = 20.5
temperature_b = 35.1

def calculate_average(temp_1, temp_2):
    """Calculate the average of two temperature values."""
    if not isinstance(temp_1, (int, float)) or not isinstance(temp_2, (int, float)):
        raise TypeError("Both temperatures must be numeric.")
    
    try:
        avg = (temp_1 + temp_2) / 2.0
    except OverflowError:
        raise ValueError("Values too large to compute average.")
    
    return round(avg, 2)

if __name__ == '__main__':
    # Hard-coded sample values as required; no user input or arguments needed.
    try:
        result = calculate_average(temperature_a, temperature_b)
        print(f"The average of the temperatures is {result} degrees.")
    except (TypeError, ValueError) as e:
        print(f"Error calculating average: {e}")