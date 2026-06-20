TARGET_NUMBER = 30

def find_exact_matches(numbers):
    return [num for num in numbers if num == TARGET_NUMBER]
if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    matches = find_exact_matches(sample_numbers)
    print(matches)