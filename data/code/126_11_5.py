def find_exact_matches(numbers, target):
    return [num for num in numbers if num == target]

if __name__ == '__main__':
    sample_numbers = [100, 200, 300, 400, 500]
    target_number = 300
    matches = find_exact_matches(sample_numbers, target_number)
    print(matches)