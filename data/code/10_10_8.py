def calculate_mean(temp1: float, temp2: float) -> str:
    """Calculate the arithmetic mean of two temperatures formatted to two decimal places."""
    return f"{(temp1 + temp2) / 2:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input or arguments needed)
    temperature_a = 25.0
    temperature_b = 30.5
    
    mean_temp = calculate_mean(temperature_a, temperature_b)
    
    print(mean_temp)