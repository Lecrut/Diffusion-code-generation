# Check if x is positive using a one-liner expression
result = lambda: bool(x) > 0
if __name__ == '__main__':
    # Test with sample values including negative, zero, and positive numbers
    for val in [-5, 0, -3.14, 2]:
        print(f"Testing x={val}: {bool(val) > 0}")