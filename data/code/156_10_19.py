import statistics

def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [12, 24, 36, 48, 60]
    empty_list = []
    single_value = [5]

    mean1 = calculate_mean(sample_values)
    mean2 = calculate_mean(empty_list)
    mean3 = calculate_mean(single_value)

    print(f"Mean of {sample_values}: {mean1}")
    print(f"Mean of {empty_list}: {mean2}")
    print(f"Mean of {single_value}: {mean3}")