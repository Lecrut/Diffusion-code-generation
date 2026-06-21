def group_by_remainder(numbers):
    groups = {0: [], 1: [], 2: []}
    for number in numbers:
        remainder = number % 3
        groups[remainder].append(number)
    return groups

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(group_by_remainder(sample_numbers))