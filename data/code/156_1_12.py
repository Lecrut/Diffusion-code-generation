def validate_data(data):
    if not data:
        raise ValueError("Input list cannot be empty")

def calculate_average(data):
    validate_data(data)
    total = 0
    count = len(data)
    for number in data:
        total += number
    return total / count

if __name__ == '__main__':
    sample_values = [15.2, 24.3, 33.4, 42.5, 51.6]
    avg = calculate_average(sample_values)
    print(f"Average of {sample_values}: {avg}")