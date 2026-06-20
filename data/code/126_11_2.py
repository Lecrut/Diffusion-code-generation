def find_exact_matches(numbers, target):
    return [num for num in numbers if num == target]

if __name__ == '__main__':
    sample_numbers = [15, 25, 35, 45, 55]
    target_number = 35
    matches = find_exact_matches(sample_numbers, target_number)
    print(matches)