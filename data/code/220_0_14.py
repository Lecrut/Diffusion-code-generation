from statistics import mean

def calculate_average_of_floats(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return mean(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5]
    average = calculate_average_of_floats(sample_numbers)
    print(average)