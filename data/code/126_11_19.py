def find_exact_matches(values, target):
    return [value for value in values if value == target]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    target_value = 30
    matches = find_exact_matches(sample_values, target_value)
    print(matches)