def calculate_mean(temp1: float, temp2: float) -> str:
    """Calculate the arithmetic mean of two temperatures formatted to two decimal places."""
    return f"{(temp1 + temp2) / 2:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values as per constraints (no user input or arguments)
    reading_a = 36.5
    reading_b = 40.7
    
    mean_result = calculate_mean(reading_a, reading_b)
    
    print(f"Mean temperature: {mean_result}")