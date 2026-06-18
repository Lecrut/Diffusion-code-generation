def validate_numeric(value):
    """Check if a string represents a valid number."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def compare_temperatures(temp_a, temp_b):
    """Compare two numeric temperatures and print the result."""
    if not validate_numeric(str(temp_a)) or not validate_numeric(str(temp_b)):
        raise TypeError("Both temperature values must be valid numbers.")

    a = float(temp_a)
    b = float(temp_b)

    results = []
    if a > b:
        results.append(f"{a} is greater than {b}")
    elif a < b:
        results.append(f"{a} is less than {b}")
    else:
        results.append(f"{a} equals {b}")

    print("\n".join(results))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    temp1 = "25"
    temp2 = "30"
    
    try:
        compare_temperatures(temp1, temp2)
    except TypeError as e:
        print(f"Validation error: {e}")