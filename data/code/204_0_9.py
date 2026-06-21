import statistics

MIDDLE_INDEX = 1

def find_middle_value(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle_index = (n - MIDDLE_INDEX) // 2
    return sorted_numbers[middle_index]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_middle_value(sample_values))