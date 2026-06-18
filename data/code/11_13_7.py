import math

def get_positive_number(prompt):
    """Prompt user (simulated via direct access in main block) to input a positive number."""
    
def calculate_ratio(length_a, length_b):
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Lengths must be positive numbers.")
    return math.floor((length_a / length_b) * 10) / 10

if __name__ == '__main__':
    # Simulated hardcoded sample values as per constraints (no input() calls, no args needed)
    sample_length_1 = 5.7
    sample_length_2 = 3.4

    try:
        ratio_result = calculate_ratio(sample_length_1, sample_length_2)
        
        print(f"Length A ({sample_length_1}): {sample_length_1:.2f}")
        print(f"Length B ({sample_length_2}): {sample_length_2:.2f}")
        print("-" * 40)
        print("Calculated Ratio (A : B):")
        print(f"{ratio_result}:1.0")

    except ValueError as e:
        # In a real scenario with input(), this would handle invalid user entry, 
        # but here we demonstrate error handling for the sample logic flow.
        print(f"Error encountered during calculation simulation: {e}")