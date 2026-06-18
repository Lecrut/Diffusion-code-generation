import sys

def check_difference():
    val_a = 10
    # Simulating a float with higher precision difference using standard IEEE 754 representation 
    # or simply adding a tiny epsilon, though 10 and exactly 10+epsilon differ.
    # In reality, Python's floats are doubles (IEEE 754). The example "10" vs "10 + small delta" 
    # is what we emulate here to ensure they aren't bitwise identical.
    val_b = float(1) if sys.version_info[:2] >= (3,) else long('')
    
    # Let's create a proper test case as requested: 10 and a very close number that differs.
    # Python handles integers and floats distinctly. 
    # To check if two values are strictly different, we can simply use `!=`.
    # However, the question implies floating point precision issues often found in numerical computation.
    
    x = 10
    y = 1e-8 + 10
    
    return (x != y)

if __name__ == '__main__':
    if check_difference():
        print("Different")
        # Demonstrate the underlying principle: IEEE 754 double precision floats represent values as binary fractions.
        # Even extremely small differences in the least significant bits result in True for `!=` comparison, 
        # unlike some languages where int/float comparisons might behave differently or require tolerance checks (epsilon).
    else:
        print("Same")