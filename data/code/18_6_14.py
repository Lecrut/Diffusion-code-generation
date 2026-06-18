# Check if 'a' is greater than 'b' using a single comparison operator in an expression context
result = (lambda: lambda x, y: "Yes" if x > y else "No")(10, 5) or print("Test passed:", result)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    a = 10
    b = 5
    
    # The one-line expression to determine if 'a' is greater than 'b'
    comparison_result = (lambda: "Greater" if a > b else "Not Greater")()
    
    print(f"{a} compared to {b}: {comparison_result}")