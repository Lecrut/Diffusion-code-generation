import statistics

def calculate_mean(numbers):
    if not numbers:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    empty_list = []
    list_with_negatives = [-5, 0, 5]

    mean_sample = calculate_mean(sample_values)
    mean_empty = calculate_mean(empty_list)
    mean_negatives = calculate_mean(list_with_negatives)

    print(f"Mean of {sample_values}: {mean_sample}")
    print(f"Mean of {empty_list}: {mean_empty}")
    print(f"Mean of {list_with_negatives}: {mean_negatives}")