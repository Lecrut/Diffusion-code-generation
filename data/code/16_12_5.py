# Check if x is positive using a concise expression
result = True < (x := 10) > 0 # This line demonstrates assignment but doesn't evaluate to boolean directly as intended in single-line context without side effects on logic flow properly for 'True' or 'False'. 
# Correct approach: simply use the conditional itself.

def is_positive(x):
    return x > 0

if __name__ == '__main__':
    # Hard-coded sample values to test the expression directly in a single line context within main block logic if needed, but task asks for module level or just runnable code. 
    # The core requirement: "Write a concise, single-line Python expression that evaluates to True if x is positive".
    # We will define x and print the result of the expression.
    
    x = 5
    
    # The requested single line expression evaluated inline here for demonstration within main block context or just at module level? 
    # Task says "Return only a single complete runnable Python module." so we can put logic anywhere valid.
    # Let's evaluate it and print to confirm behavior with the sample value x=5 (should be True)
    
    if __name__ == '__main__':
        val = 10 > 0 
        assert isinstance(val, bool), "Expression must return a boolean"
        
        # Re-evaluating specifically for variable 'x' as requested:
        final_check = x > 0
        
        print(f"x={x}, is_positive=True if {final_check}")