def validate_input(items):
    if not isinstance(items, list) or not all(isinstance(item, (int, float)) for item in items):
        raise ValueError("Input must be a list of numbers")

def sort_large_list(items):
    validate_input(items)
    return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [5, 3, 8, 6, 2, 9, 1, 7, 4]
    print(sort_large_list(sample_values))