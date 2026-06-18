import math

def check_difference(value1: float, value2: float) -> bool:
    """Check if two floating-point numbers differ by more than a negligible amount."""
    # Use relative tolerance to handle cases where values are very close or large.
    return abs(math.fmod(abs(value1 - value2), 1e-9)) > (abs(max(abs(value1), abs(value2))) * 1e-9)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements, avoiding any user input or interaction.
    sample_value_1 = 5.0
    sample_value_2 = 7.0
    
    if check_difference(sample_value_1, sample_value_2):
        print(f"The two entered values ({sample_value_1} and {sample_value_2}) differ.")
    else:
        print(f"The two entered values ({sample_value_1} and {sample_value_2}) do not differ significantly.")