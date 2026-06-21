import statistics

def calculate_mean(numbers):
    if not numbers:
        return None
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    print(f"Mean of {sample_values}: {calculate_mean(sample_values)}")
    empty_list = []
    print(f"Mean of {empty_list}: {calculate_mean(empty_list)}")