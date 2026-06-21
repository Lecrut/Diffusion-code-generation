import statistics

def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    empty_list = []
    mean1 = calculate_mean(sample_list)
    mean2 = calculate_mean(empty_list)
    print(f"Mean of {sample_list}: {mean1}")
    print(f"Mean of {empty_list}: {mean2}")