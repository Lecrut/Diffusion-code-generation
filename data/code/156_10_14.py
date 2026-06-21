import statistics

def calculate_average(numbers):
    return statistics.mean(numbers) if numbers else 0

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(calculate_average(sample_numbers))
    empty_list = []
    print(calculate_average(empty_list))