import statistics
DEFAULT_LIST = [1, 2, 3, 4, 5]

def calculate_mean(numbers):
    return statistics.mean(numbers)
if __name__ == '__main__':
    sample_lists = [DEFAULT_LIST, [], [10.5, 20.5, 30.5], [-1, 5, 10, -5]]
    for sample_list in sample_lists:
        mean_value = calculate_mean(sample_list)
        print(f'Mean of {sample_list}: {mean_value}')