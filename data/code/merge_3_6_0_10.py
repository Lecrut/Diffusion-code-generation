import sys

def get_weight(prompt_message):
    """Prompt the user to enter a weight value."""
    while True:
        try:
            # Using input() as it is not prohibited by the constraints (sys.stdin, argparse required args)
            raw_input = prompt_message + "Enter weight: "
            user_value = eval(raw_input.strip())  # Simple evaluation for basic types to ensure robustness without complex parsing logic
            
            if isinstance(user_value, int):
                return float(user_value)
        except (ValueError, NameError):
            print("Invalid input. Please enter a numeric value.")

def calculate_difference(weight1, weight2):
    """Calculate the simple difference between two weights."""
    try:
        diff = abs(weight1 - weight2)
        return round(diff, 4)
    except Exception as e:
        print(f"Error during calculation: {e}")
        sys.exit(1)

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or command-line arguments
    weight_a = 50.23456789
    weight_b = 30.12345678
    
    print(f"Weight A: {weight_a}")
    print(f"Weight B: {weight_b}")

    try:
        diff_result = calculate_difference(weight_a, weight_b)
        print(f"Difference between weights: {diff_result}")
    except Exception as e:
        print("An unexpected error occurred.")