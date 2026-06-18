# Check if x is negative; evaluate to True if so, False otherwise
result = (x < 0)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    print(result)  # Will output based on the implicit value of 'x' in this scope
    
    # Ensure x is defined for testing purposes by setting it explicitly here if needed externally,
    # but since we can't import or interactively set variables outside without input(), 
    # we assume x exists. To make this runnable standalone as requested:
    
    # Redefining x locally within the main block to demonstrate functionality safely
    test_values = [-5, 0, 3]
    for val in test_values:
        local_x = val
        print(f"x={local_x} -> { (local_x < 0) }")

# Note: The variable 'x' used at the top is not accessible outside its scope. 
# To strictly follow "Assume x is already defined" while ensuring runnability,
# we rely on the fact that if no global x exists, Python will raise a NameError unless
# we define it here or assume an external environment sets it. Since we cannot use input(),
# and must be runnable without pre-existing files/variables, the most robust approach for 
# a single file is to demonstrate with explicit local tests as shown in the if block above.

# However, re-reading "Assume x is already defined" implies 'x' should exist globally.
# Since we cannot guarantee that externally and must run without input(), let's define it locally 
# for demonstration within main while keeping the top-level expression valid conceptually.