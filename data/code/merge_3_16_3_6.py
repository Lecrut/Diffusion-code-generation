if __name__ == '__main__':
    x = 5 if True else -3
    
def is_positive(x):
    return bool(x > 0)

print(is_positive(x)) # Should print False when x=-3, but we need to test both cases in one line logic as per task requirement for the expression itself. 
# The core request was a ONE-LINE EXPRESSION that evaluates True if positive else False.
# Let's re-read: "Write a concise, one-line Python expression". This usually means just the expression code, not necessarily inside main block unless specified to demonstrate it works.
# However, the instruction says "Return only a single complete runnable Python module." and "Include an `if __name__ == '__main__':` block with hard-coded sample values."
# And "The sample block must run without user input...".

# Let's create a script that defines x in main to demonstrate. 
# But wait, the task says "Assume x is already defined" for the expression part.
# The module should contain the one-line expression AND the test block.

x = 10 # Sample positive value
result_expr = (lambda: bool(x > 0))() 

print(f"x={x}, Expression result: {result_expr}")

if __name__ == '__main__':
    x_test_1, x_test_2 = -5, 3
    
    def check_positive(val):
        return val > 0
        
    print(check_positive(x_test_1)) # False
    print(check_positive(x_test_2)) # True