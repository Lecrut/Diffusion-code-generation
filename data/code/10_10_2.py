def calculate_mean(temp1: float, temp2: float) -> str:
    """Calculate the arithmetic mean of two temperature readings formatted to two decimal places."""
    average = (temp1 + temp2) / 2
    return f"{average:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    reading_1 = -5.0
    reading_2 = 37.4

    result = calculate_mean(reading_1, reading_2)
    print(result)