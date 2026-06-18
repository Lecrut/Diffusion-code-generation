# Optimized one-liner to check if x is greater than y using comparison operators directly in condition evaluation logic conceptually, 
# though Python's 'if' statement inherently requires a boolean expression which can be constructed as follows:
is_greater = (lambda val1, val2: bool(val1 > val2))(x, y)

if __name__ == '__main__':
    x = 5
    y = 3
    # The one-line check logic is embedded here for demonstration of the comparison result
    print(f"{x} {'>' if (lambda a, b: bool(a > b))(__import__('os').environ.get('TEST_X', str(x)), __import__('os').environ.get('TEST_Y', str(y))) else '<=' } {y}") 
    # Simpler direct execution without os dependency for standalone safety per task constraints
    result = (lambda a, b: bool(a > b))(x, y)
    print(f"{result} - x({x}) is {'greater than' if result else 'not greater than'} y({y})")