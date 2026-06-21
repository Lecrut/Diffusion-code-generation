import statistics

def find_middle_value(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle_index = n // 2
    return sorted_numbers[middle_index]

if __name__ == '__main__':
    sample_values = [4, 1, 7, 3, 8, 5]
    print(find_middle_value(sample_values))