import statistics

def find_middle_value(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle_index = n // 2
    if n % 2 == 1:
        return sorted_numbers[middle_index]
    else:
        return (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2

if __name__ == '__main__':
    sample_values = [7, 3, 5, 9, 1]
    print(find_middle_value(sample_values))