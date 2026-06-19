def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.

    Args:
        side_length (float or int): The length of one side of the square.

    Returns:
        float: The calculated area of the square.

    Raises:
        TypeError: If side_length is not an instance of float or int.
        ValueError: If side_length is negative.
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be a number.")
    
    if side_length < 0:
        raise ValueError("side_length cannot be negative.")

    return side_length ** 2

if __name__ == '__main__':
    # Sample values for testing the function without any user input or external dependencies.
    sample_inputs = [5, 10.5, -3]

    results = []
    try:
        for val in sample_inputs:
            area = calculate_square_area(val)
            results.append(f"Area of square with side {val}: {area}")
    except (TypeError, ValueError) as e:
        print(f"Error calculating for input {val}: {e}")

    # Printing all successful or error messages to demonstrate functionality.
    print("Calculations:")
    if len(results) > 0:
        print("\n".join(results))
    else:
        print("(No areas calculated)")