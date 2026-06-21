def find_median(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
    else:
        return sorted_numbers[mid]

if __name__ == '__main__':
    sample_input = [10, 5, 20, 15, 30]
    try:
        number_list = []
        for item in sample_input:
            number_list.append(int(item))
        median_value = find_median(number_list)
        print(median_value)
    except ValueError:
        print("Invalid input")