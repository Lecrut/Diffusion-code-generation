def calculate_ratio():
    """Reads two length measurements from a predefined list (simulating input),
    validates they are positive numbers, and prints their ratio."""
    
    # Hard-coded sample values to simulate user input without interactive prompts
    first_measurement = 10.5
    second_measurement = 24

    try:
        result = first_measurement / second_measurement
        print(f"The ratio of {first_measurement} to {second_measurement} is {result}")
    except ZeroDivisionError:
        # Handles the case where division by zero occurs, though input validation prevents it here.
        print("An error occurred during calculation.")

if __name__ == '__main__':
    calculate_ratio()