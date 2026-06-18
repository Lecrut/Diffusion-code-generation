def calculate_mean(temp1: float, temp2: float) -> str:
    """Calculate the arithmetic mean of two temperature readings formatted to two decimal places."""
    return f"{(temp1 + temp2) / 2:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access).
    reading_a = 25.678
    reading_b = 30.129
    
    mean_temperature = calculate_mean(reading_a, reading_b)
    
    print(mean_temperature)