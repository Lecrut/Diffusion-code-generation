def compute_median(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle_index = length // 2
    if length % 2 == 1:
        return sorted_numbers[middle_index]
    else:
        return (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) // 2

if __name__ == '__main__':
    print(compute_median([3, 1, 2]))
    print(compute_median([4, 1, 3, 2]))
    print(compute_median([7, 8, 9]))
    print(compute_median([10, 20, 30, 40]))
    print(compute_median([5]))