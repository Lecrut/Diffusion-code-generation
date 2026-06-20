import numpy as np

def average_with_error_handling(numbers):
    numbers = np.array(numbers)
    count = len(numbers)
    if count == 0:
        return None
    sum_of_numbers = np.sum(numbers)
    try:
        avg = sum_of_numbers / count
    except ZeroDivisionError:
        return None
    return avg

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    result = average_with_error_handling(sample_values)
    print(result)