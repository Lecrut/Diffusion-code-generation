MEAN_EMPTY_LIST = None

def calculate_mean(numbers):
    if not numbers:
        return MEAN_EMPTY_LIST
    total_sum = sum(numbers)
    count = len(numbers)
    mean_value = total_sum / count
    return mean_value

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_values))
    empty_list = []
    print(calculate_mean(empty_list))