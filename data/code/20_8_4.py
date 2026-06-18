def compare_values():
    """Compares two values based on exact type matching."""
    
# Hard-coded sample values to run without user input
value_a = 10
value_b = "10"

print(f"Value A: {value_a} (Type: {type(value_a).__name__})")
print(f"Value B: {value_b} (Type: {type(value_b).__name__})")

# Check if types are exactly the same using type() and direct comparison
if type(value_a) == type(value_b):
    # Then check equality directly
    result = value_a == value_b
else:
    result = False

print(f"Are they equal with exact type matching? {result}")

if __name__ == '__main__':
    compare_values()