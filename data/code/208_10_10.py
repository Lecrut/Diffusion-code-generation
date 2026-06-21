import statistics

MEAN_EMPTY = None

def calculate_mean(numbers):
    if not numbers:
        return MEAN_EMPTY
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values1 = [1, 2, 3, 4, 5]
    sample_values2 = [10.5, 20.5, 30.5]
    empty_list = []
    print(f"Mean of {sample_values1}: {calculate_mean(sample_values1)}")
    print(f"Mean of {sample_values2}: {calculate_mean(sample_values2)}")
    print(f"Mean of {empty_list}: {calculate_mean(empty_list)}")