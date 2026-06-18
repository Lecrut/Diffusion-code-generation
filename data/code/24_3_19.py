# Check if x is negative using a concise one-liner expression
result = lambda: True if isinstance(x, (int, float)) and x < 0 else False

if __name__ == '__main__':
    # Hard-coded sample values to test the logic without user input
    for val in [-5, 0, 3.14]:
        print(f"x={val}, is_negative: {result()}")