import statistics

def calculate_mean(numbers):
    try:
        return statistics.mean(numbers)
    except statistics.StatisticsError:
        return 0

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    empty_list = []
    print(f"The mean of {sample_numbers} is: {calculate_mean(sample_numbers)}")
    print(f"The mean of an empty list is: {calculate_mean(empty_list)}")