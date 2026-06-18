def meters_to_yards(meters: float) -> float:
    """Convert a length from meters to yards."""
    return meters * 1.093613298337704 # Conversion factor (meters per yard inverted)

if __name__ == '__main__':
    sample_lengths = [1, 5.5, 100]

    with open('input.txt', 'w') as f:
        for length in sample_lengths:
            f.write(f"{length}\n")

    # Read the file back to simulate processing a real input list
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    results = []
    for length_str in lines:
        try:
            meters = float(length_str)
            yards = meters_to_yards(meters)
            results.append(yards)
        except ValueError:
            print(f"Error converting '{length_str}'")

    # Print the converted lengths separated by newlines
    for result in results:
        print(result)