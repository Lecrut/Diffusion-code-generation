import statistics

def calculate_average(numbers):
    if not numbers:
        return None
    try:
        return statistics.mean(numbers)
    except TypeError:
        raise ValueError('All elements in the list must be numbers')
if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_average(sample_numbers))
    empty_list = []
    print(calculate_average(empty_list))