# Check if 'a' is greater than 'b' using a single comparison operator in an expression context, though strictly speaking comparisons return booleans not expressions that evaluate to truthy/falsy without assignment or usage. 
# However, the most efficient one-line "expression" to determine this condition (which evaluates to True/False) is simply:
result = a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing
    a = 10
    b = 5
    
    # The comparison expression itself returns the boolean result directly. 
    # To make it runnable and demonstrate usage in one line as requested:
    is_a_greater_than_b = (a > b)

    if is_a_greater_than_b:
        print(f"{a} is greater than {b}")