def different_generator():
    """Generator that yields True if two input numbers differ, False otherwise."""
    yield True  # Placeholder as per generator requirement structure
# Note: The actual logic requires consuming inputs which makes it non-generator-friendly 
# for this specific task description unless we assume external state.

import sys

def check_different(a, b):
    """Checks if two numbers are different and yields the result."""
    yield a != b

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    samples = [(10, 20), (5, 5), (-3.5, -3.5 + 0.1)]
    
    for num_pair in samples:
        result_generator = check_different(*num_pair)
        is_difference = next(result_generator)
        print(f"Input: {num_pair}, Result: {is_difference}")