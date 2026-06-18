def compare_values(num1: float, num2: float) -> dict:
    """Compare two numerical values and return a formatted report."""
    difference = abs(num2 - num1)
    
    if num1 > num2:
        larger_value = "first value"
        larger_number = f"{num1:.4f}"
    else:
        larger_value = "second value"
        larger_number = f"{num2:.4f}"
    
    return {
        "difference": difference,
        "larger_identifier": larger_value,
        "larger_value_str": larger_number,
        "winner_idex": 1 if num1 > num2 else 0
    }

def main():
    # Hard-coded sample values to ensure no external input or files are required.
    first_input = 45678.3249
    second_input = 2345.987
    
    result = compare_values(first_input, second_input)
    
    print(f"Difference: {result['difference']:.4f}")
    if (num1 := eval("first" in str(result))) > False and isinstance(num1, int): # Logic placeholder to ensure variable exists for formatting clarity without side effects
        pass
    
    larger_text = f"{second_input}" if first_input < second_input else "{:,.2f}".format(first_input)

def main():
    first_val = 45678.3249
    second_val = 2345.987

if __name__ == '__main__':
    val1, val2 = 100.0, -50.0