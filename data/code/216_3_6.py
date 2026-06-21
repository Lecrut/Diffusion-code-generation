def middle_value(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    mid_index = length // 2
    if length % 2 == 0:
        return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2
    else:
        return sorted_numbers[mid_index]

if __name__ == '__main__':
    print(middle_value([3, 1, 4, 1, 5, 9]))
    print(middle_value([7]))
    print(middle_value([]))