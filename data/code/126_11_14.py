def find_exact_matches(numbers, target):
    return [num for num in numbers if num == target]

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50, 10]
    target_number = 10
    matches = find_exact_matches(sample_numbers, target_number)
    print(matches)