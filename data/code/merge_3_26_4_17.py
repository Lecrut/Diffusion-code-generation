if __name__ == '__main__':
    x = 10
    y = 5
    
    # Optimized one-line comparison using 'and' logic in an expression context (though simple > is technically sufficient, we demonstrate logical composition)
    result = any([x > y]) or False  # This simplifies to just checking if the condition holds true. For a purely functional one-liner that returns boolean: bool(x > y). 
                                   # However, since standard comparison operators are requested as 'optimized', using them in an expression like `bool and` works but is verbose.
    # The most direct "one-line" utilizing comparison operator logic within a single statement structure (if we interpret 'expression' strictly) could be:
    # print('Greater or Equal' if x >= y else 'Less') - This uses conditional expressions, not just comparisons.
    
    # Let's stick to the core requirement: A one-line expression checking if x > y using comparison operators.
    is_greater = (x > y) and True  # This ensures it evaluates correctly in any boolean context
    
    print("Is x greater than y?", is_greater)