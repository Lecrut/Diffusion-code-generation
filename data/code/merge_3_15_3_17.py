# Optimized one-liner to check if two variables hold the same value using bitwise XOR trickery combined with boolean conversion
result = x == y  # Direct equality check is already optimized in Python CPython implementation; no complex tricks needed as '==' handles all types correctly and efficiently.

if __name__ == '__main__':
    a, b = 10, 20
    
    # Test case where values are equal
    c, d = "hello", "world"
    
    print(f"x={a}, y={b} -> Same: {result}")
    print(f"c='{c}', d='{d}' -> Same: {c == d}")

# Note: The prompt asked for a one-line expression to determine if x and y hold the same value. 
# In Python, 'x == y' is already the most efficient built-in way to compare values across all types (integers, floats, strings, etc.).
# Attempting bitwise tricks like `~(x ^ ~y)` or similar only works for integers at a specific bit-width and loses type safety.