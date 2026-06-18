def calculate_mean(temp1: float, temp2: float) -> str:
    """Calculates the arithmetic mean of two temperature readings formatted to two decimal places."""
    mean_value = (temp1 + temp2) / 2
    return f"{mean_value:.2f}"

if __name__ == '__main__':
    # Sample values provided directly without any user input prompts or file access.
    reading_a: float = 98.65
    reading_b: float = 100.37
    
    result_str = calculate_mean(reading_a, reading_b)
    
    print(result_str)