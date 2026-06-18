def is_numeric(value):
    """Check if a string represents a valid number."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def compare_temperatures(temp1, temp2):
    """Compare two numeric temperatures and determine the relationship."""
    result = ""
    if temp1 == temp2:
        result = "The temperatures are equal."
    elif temp1 > temp2:
        difference = f"{temp1 - temp2:.2f}"
        result = f"Temperature {temp1} is higher than {temp2} by {difference} degrees."
    else:
        difference = f"{abs(temp2 - temp1):.2f}"
        result = f"Temperature {temp2} is higher than {temp1} by {difference} degrees."
    return result

if __name__ == '__main__':
    sample_temp_1 = "365"
    sample_temp_2 = "-40"

    # Validate inputs (simulating user input with hardcoded values)
    if not is_numeric(sample_temp_1):
        raise ValueError("First temperature value must be numeric.")
    if not is_numeric(sample_temp_2):
        raise ValueError("Second temperature value must be numeric.")

    temp_values = [float(x) for x in [sample_temp_1, sample_temp_2]]
    
    # Print formatted result
    print(compare_temperatures(temp_values[0], temp_values[1]))