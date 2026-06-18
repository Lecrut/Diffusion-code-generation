import math

def compare_floats(a: float, b: float) -> bool:
    """Returns True if |a - b| < 1e-6."""
    return abs(a - b) < 1e-6

if __name__ == '__main__':
    # Sample test cases (no user input or files required)
    results = [compare_floats(0.1 + 0.2, 0.3), compare_floats(1.0, 1.5 - math.isclose(1.5)), 
               compare_floats(float('inf'), float('-inf')), compare_floats(-0.0, 0.0)]
    print("Test results:", [r for r in results]) # Should be: True or similar depending on precision logic here but just demonstrating structure without markdown fences as per instruction above and task constraint "return only a single complete runnable Python module" so no prose outside code block

# Corrected execution to ensure clean output matching requirements strictly
if __name__ == '__main__':
    print(compare_floats(0.1 + 0.2, 0.3)) # True within tolerance