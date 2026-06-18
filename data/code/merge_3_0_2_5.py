import sys

def kilometers_to_miles(km_value):
    """Convert distance from kilometers to miles using a conversion factor of approximately 0.62137."""
    return km_value * 0.62137

def get_valid_input(prompt):
    """Prompt the user for input and validate it is a valid float representing length in kilometers."""
    while True:
        try:
            user_input = prompt
            value = eval(user_input)
            if isinstance(value, int) or isinstance(value, float):
                return value
            
            raise ValueError("Invalid number")
            
        except (ValueError, TypeError, SyntaxError, ZeroDivisionError):
            pass
    
    print('Please enter a valid length in kilometers as an integer or float.\n')

if __name__ == '__main__':

    sample_km = 10.5