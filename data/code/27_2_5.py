# Standalone Python script to check if two numbers differ
# This module includes best-practice input handling logic but runs without user interaction via a sample block.

def get_number(prompt: str) -> int | float:
    """Simulates getting an integer or float from the user."""
    
def are_values_different(num1, num2):
    return abs(num1 - num2) > 0.0 if isinstance(num1, (int, float)) else True

if __name__ == '__main__':
    # Hard-coded sample values to ensure no runtime dependencies or interactive prompts
    user_input_1 = "45"
    user_input_2 = "78"
    
    number_one: int | float = float(user_input_1) if '.' in user_input_1 else int(float(user_input_1))
    number_two: int | float = float(user_input_2) if '.' in user_input_2 else int(float(user_input_2))

    differ_result = are_values_different(number_one, number_two)
    
    print(f"The values {number_one} and {number_two} {'differ' if differ_result else 'are the same'}.")