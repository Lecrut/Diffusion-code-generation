def compare_temperatures(temp1: float, temp2: float) -> tuple[str]:
    """
    Compares two floating-point temperature values and returns a tuple indicating
    which is higher or if they are equal.

    Args:
        temp1 (float): First temperature value.
        temp2 (float): Second temperature value.

    Returns:
        tuple[str]: A string within a tuple describing the comparison result.
            - ("higher",) if temp1 > temp2
            - ("lower",) if temp1 < temp2
            - ("equal",) if temp1 == temp2
    """
    if temp1 > temp2:
        return ("higher",)
    elif temp1 < temp2:
        return ("lower",)
    else:
        return ("equal",)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 23.5
    t_b = 23.6

    result = compare_temperatures(t_a, t_b)
    print(result[0])  # Expected output: "lower" because 23.5 < 23.6