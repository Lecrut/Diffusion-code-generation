def find_exact_matches(numbers, target):
    return [num for num in numbers if num == target]

if __name__ == '__main__':
    sample_numbers = [12, 24, 36, 48, 60]
    target_number = 36
    matches = find_exact_matches(sample_numbers, target_number)
    print(matches)