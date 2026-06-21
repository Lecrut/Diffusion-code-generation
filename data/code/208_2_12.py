MEAN_CALCULATION_ERROR = "Unable to calculate mean"

def calculate_mean(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_values))
    empty_list = []
    result = calculate_mean(empty_list)
    if result is None:
        print(MEAN_CALCULATION_ERROR)
    else:
        print(result)