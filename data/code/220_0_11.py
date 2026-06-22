from statistics import mean

def calculate_mean(numbers: list) -> float:
    if not numbers:
        raise ValueError("Input list is empty")
    return mean(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    try:
        result = calculate_mean(sample_values)
        print(result)
    except ValueError as e:
        print(e)