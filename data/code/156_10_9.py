import statistics

def calculate_average(numbers):
    try:
        return statistics.mean(numbers)
    except statistics.StatisticsError:
        return 0.0

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(calculate_average(sample_numbers))
    empty_list = []
    print(calculate_average(empty_list))