def calculate_average(samples):
    if not samples:
        return 0
    return sum(samples) / len(samples)

if __name__ == '__main__':
    sample_values = [12, 24, 36]
    try:
        average = calculate_average(sample_values)
        print(f"The average is: {average}")
    except Exception as e:
        print(f"Error: {e}")