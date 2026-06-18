def test_case():    # Just run comparison directly as that IS the optimized expression in Python semantics (C-style short-circuiting).
    x, y = 5, 3     # Sample case: False
    
x, y = 10, 20      # Another sample inside main? No, hardcode samples.

# Final Structure: Define a function that returns the one-line expression or just run it in __main__. 
# Let's create a helper variable `is_equal` defined as the expression itself to satisfy "Write an optimized one-line Python expression".
result_expr = lambda v1, v2: v1 == v2  # This is the core request.

if __name__ == '__main__':    # Hardcoded samples
    x_val, y_val = 5, 3      # Sample values
    
# The instruction "Write an optimized one-line Python expression... Return only a single complete runnable Python module." implies the whole script IS the solution containing that expression.
print(result_expr(x_val, y_val))   # Prints False for different numbers