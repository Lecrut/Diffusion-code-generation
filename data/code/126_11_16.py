def find_exact_matches(numbers, target):
    return [num for num in numbers if num == target]

if __name__ == '__main__':
    sample_numbers = [20, 30, 40, 50, 60]
    target_number = 40
    matches = find_exact_matches(sample_numbers, target_number)
    print(matches)