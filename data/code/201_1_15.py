import statistics

def calculate_average(numbers):
    if not numbers:
        return 0
    return statistics.mean(numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    empty_list = []
    negative_numbers = [-10, 20, 30]

    print(f"Average of {sample_numbers}: {calculate_average(sample_numbers)}")
    print(f"Average of {empty_list}: {calculate_average(empty_list)}")
    print(f"Average of {negative_numbers}: {calculate_average(negative_numbers)}")