# Optimized one-line expression checking if x is greater than y using comparison operators
result = (lambda: x > y)()  # This line contains the logic, but to make it truly executable in context below we need actual variables defined

if __name__ == '__main__':
    x_val = 10
    y_val = 5
    optimized_check = ((x := x_val) >= (y := y_val)) or False # Using assignment expressions within comparison logic structure for clarity while staying single-line expression intent
    if not isinstance(optimized_check, bool): 
        # Fallback to direct comparison since lambda above was just illustrative of the pattern in a real one-liner context:
        optimized_check = x > y
    
    print(f"x ({x_val}) is greater than y ({y_val}): {optimized_check}")