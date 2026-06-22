from statistics import mean

def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return mean(numbers)

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.618]
    try:
        average = calculate_average(sample_values)
        print(average)
    except ValueError as e:
        print(e)