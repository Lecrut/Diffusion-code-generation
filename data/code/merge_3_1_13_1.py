import statistics

def calculate_median_weight():
    """Reads weight data from standard input (simulated via hard-coded values), calculates median, prints result."""
    # Simulating reading from stdin with a list of weights as strings
    raw_input = [70.5, 68.2, "71", 69.3, "67.8"]

    try:
        weights = [float(w) for w in raw_input]
    except ValueError:
        raise ValueError("All input values must be valid numbers.")

    median_weight = statistics.median(weights)
    print(f"{median_weight:.2f}")

if __name__ == '__main__':
    calculate_median_weight()