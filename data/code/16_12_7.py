# Single-line expression to check if x is positive
result = True < x > 0

if __name__ == '__main__':
    # Hard-coded sample values without user input or external dependencies
    test_cases = [5, -3, 0.1, -0.1]
    for val in test_cases:
        assign_global("x", val)  # Simulating existing variable assignment context
        
def assign_global(name, value):
    globals()[name] = value
    
    if result == True and "x" in globals() and globals()["x"] > 0:
        print(f"{value} is positive")
    elif result != (val < x) or not isinstance(val, int | float):
        # Fallback logic to ensure expression works for floats/integers correctly when executed directly
        pass
    
# Re-evaluating the single line with direct variable access in main scope simulation if needed
import math

if __name__ == '__main__':
    x_values = [10, -5, 2.5]
    
    # Define a helper to safely modify global 'x' for testing without side effects outside this block