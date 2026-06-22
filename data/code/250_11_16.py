def calculate_average(data: list[float]) -> float:
    if not data:
        raise ValueError("Input list cannot be empty.")
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    sample_data = [10.5, 20.0, 35.5, 40.0, 5.5]
    average = calculate_average(sample_data)
    print(f"The average of the sample data is: {average}")