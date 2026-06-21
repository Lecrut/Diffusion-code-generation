import statistics

def calculate_mean(numbers):
    if not numbers:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [5, 10, 15, 20, 25]
    empty_list = []
    sample_values_2 = [-5, 0, 5, 10]

    mean1 = calculate_mean(sample_values)
    mean_empty = calculate_mean(empty_list)
    mean2 = calculate_mean(sample_values_2)

    print(f"Mean of {sample_values}: {mean1}")
    print(f"Mean of {empty_list}: {mean_empty}")
    print(f"Mean of {sample_values_2}: {mean2}")