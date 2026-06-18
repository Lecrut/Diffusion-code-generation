def meters_to_yards(meters: float) -> str:
    """Convert a given length in meters to yards."""
    return f"{meters / 0.9144:.2f} yards"

if __name__ == '__main__':
    sample_lengths = [1, 5, 36.73]

    with open('input.txt', 'w') as output_file:
        for length in sample_lengths:
            converted_length = meters_to_yards(length)
            print(f"{length} meters is {converted_length}", end=" ")