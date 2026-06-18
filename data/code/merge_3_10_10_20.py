def calculate_mean(temp1: float, temp2: float) -> float:
    """Calculate the arithmetic mean of two temperature readings."""
    return (temp1 + temp2) / 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    reading_a = 98.6
    reading_b = 99.0

    mean_temp = calculate_mean(reading_a, reading_b)

    # Format the output to two decimal places and print it.
    formatted_output = f"{mean_temp:.2f}"
    print(formatted_output)