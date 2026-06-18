# Determine if 'a' is greater than 'b' using a single comparison operator
result = (1 < 2) # This line demonstrates the syntax, but we need actual variables in main block below

if __name__ == '__main__':
    # Define sample values without any user input or external dependencies
    a = 10
    b = 5
    
    # The task asks for an expression to determine if 'a' > 'b'. 
    # While (a > b) is the direct answer, let's create a slightly more complex but efficient one-liner 
    # that still uses comparison operators effectively as requested. 
    # However, strictly following "one-line expression using Python's comparison operators",
    # the most accurate and efficient representation for checking 'a' vs 'b' is simply: (a > b)
    
    # To make it a meaningful script while adhering to constraints, we evaluate the condition directly.
    cond = (a > b)
    
    if cond:
        print(f"{a} is greater than {b}")
    else:
        print(f"{a} is not greater than {b}" or f"{a} equals or is less than {b}", end="") # Using logical operator to handle the false case gracefully in one output line logic, though strictly comparison was requested.