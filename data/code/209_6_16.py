def calculate_average(samples):
    return sum(samples) / len(samples)

if __name__ == '__main__':
    sample_values = [12, 24, 36]
    try:
        average = calculate_average(sample_values)
        print(f"The average is: {average}")
    except ZeroDivisionError:
        print("Error: Sample list cannot be empty.")