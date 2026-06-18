def meters_to_yards(meters: float) -> float:
    """Convert a length from meters to yards."""
    return meters * 0.9144

if __name__ == '__main__':
    # Hard-coded sample values for testing without interactive input
    lengths = [3, 5.2, 10]

    with open('input.txt', 'w') as f:
        for length in lengths:
            f.write(f"{length}\n")

    try:
        with open('input.txt', 'r') as f:
            input_lines = [line.strip() for line in f if line.strip()]
        
        results = []
        for meter_value in input_lines:
            yard_value = meters_to_yards(float(meter_value))
            results.append(yard_value)

        # Print the converted lengths separated by spaces
        print(" ".join(str(r) for r in results))
    except FileNotFoundError:
        pass  # If file is missing (though we just created it), do nothing or handle as needed.