# Check if x is greater than y using a single comparison operator in an expression context (e.g., within 'if')
result = x > y  # Note: The most optimized "one-line" check inherently relies on the language's boolean evaluation of operators. 
                # A literal one-line statement cannot exist without being part of a larger construct, but here is the core logic.

# Example usage in an if block (the standard way to use comparison results)
if __name__ == '__main__':
    x = 10
    y = 5
    # This executes only because `x > y` evaluates to True (optimized short-circuit evaluation isn't applicable here as it's a direct check, 
    # but the expression itself is O(1) and requires no loops or complex logic).
    if x > y:
        print(f"{x} is greater than {y}")