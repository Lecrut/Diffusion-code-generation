MATCHES_FOUND = "Matches found"
NO_MATCHES = "No matches"

def find_exact_matches(numbers, target):
    matches = [num for num in numbers if num == target]
    return MATCHES_FOUND if matches else NO_MATCHES

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    target_number = 30
    result = find_exact_matches(sample_numbers, target_number)
    print(result)