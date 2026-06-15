def compute_average(samples):
    if not samples:
        return 0
    return sum(samples) / len(samples)
if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    try:
        sample_strings = sample_input.split()
        numbers = []
        for s in sample_strings:
            numbers.append(float(s))
        average = compute_average(numbers)
        print(f"The average is: {average}")
    except ValueError:
        print("Error: One or more inputs were not valid numbers.")