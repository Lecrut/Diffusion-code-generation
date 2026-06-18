import sys

def compare_values():
    """Compares two values based on exact type matching."""
    
# Hard-coded sample values to ensure no user input is required
value_a = 42
value_b = "42"

def are_equal_exact_type(val1, val2):
    """Returns True if both value and type match exactly."""
    return (val1 == val2) and (type(val1) == type(val2))

if __name__ == '__main__':
    result = are_equal_exact_type(value_a, value_b)
    
# Output the result without printing prompts or requiring input
print(f"Value {value_a} ({type(value_a).__name__}) equals Value {value_b} ({type(value_b).__name__}):", "True" if result else "False")

sys.exit(0 if result else 1)