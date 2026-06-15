def compute_average(samples):
    if not samples:
        return 0
    return sum(samples) / len(samples)
if __name__ == '__main__':
    sample_input = "10 20 30 40"
    try:
        samples = [float(x) for x in sample_input.split()]
        average = compute_average(samples)
        print(f"The average is: {average}")
    except ValueError:
        print("Error: One or more inputs were not valid numbers.")