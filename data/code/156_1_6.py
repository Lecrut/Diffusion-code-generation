def calculate_average(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    sample_values = [15.2, 24.3, 33.4, 42.5, 51.6]
    try:
        avg = calculate_average(sample_values)
        print(f"Average of {sample_values}: {avg}")
    except ValueError as e:
        print(f"Error: {e}")