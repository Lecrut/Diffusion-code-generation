def calculate_average(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    try:
        avg = calculate_average(sample_values)
        print(f"Average of {sample_values}: {avg}")
    except ValueError as e:
        print(f"Error: {e}")