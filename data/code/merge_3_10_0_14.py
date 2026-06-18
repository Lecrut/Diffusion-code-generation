def calculate_average_temperature(temp1: float, temp2: float) -> float:
    """Calculate the average of two temperature values."""
    return (temp1 + temp2) / 2

if __name__ == '__main__':
    # Hard-coded sample temperatures as per requirements to avoid user input or command-line arguments.
    SAMPLE_TEMP_1 = 23.5
    SAMPLE_TEMP_2 = -4.0

    try:
        avg_temp = calculate_average_temperature(SAMPLE_TEMP_1, SAMPLE_TEMP_2)
        print(f"The average of {SAMPLE_TEMP_1} and {SAMPLE_TEMP_2} is {avg_temp:.2f}")
    except Exception as e:
        # Generic error handling for unexpected failures during calculation.
        print(f"An error occurred while calculating the temperature average: {e}")

# Note: The script above uses hard-coded values to satisfy all constraints regarding input methods 
# and ensures no external dependencies or network access are required.