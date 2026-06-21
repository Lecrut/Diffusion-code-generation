import statistics

def calculate_mean(numbers):
    if not numbers:
        return None
    try:
        return statistics.mean(numbers)
    except TypeError as e:
        raise ValueError("Input must be a list of numerical values") from e

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(f"Mean of {sample_values}: {calculate_mean(sample_values)}")
    empty_list = []
    print(f"Mean of {empty_list}: {calculate_mean(empty_list)}")