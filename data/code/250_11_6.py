def calculate_average(data: list[float]) -> float:
    if not data:
        raise ValueError("Input list cannot be empty.")
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    sample_data = [15.2, 23.4, 37.8, 41.6, 6.9]
    average = calculate_average(sample_data)
    print(f"The average of the sample data is: {average}")