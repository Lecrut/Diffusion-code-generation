import statistics

def calculate_average(numbers):
    try:
        return statistics.mean(numbers)
    except statistics.StatisticsError:
        return 0

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(f"The average of {sample_numbers} is: {calculate_average(sample_numbers)}")
    empty_list = []
    print(f"The average of an empty list is: {calculate_average(empty_list)}")