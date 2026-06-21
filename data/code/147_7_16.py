def validate_input(items):
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
    for item in items:
        if not isinstance(item, (int, float)):
            raise ValueError("All items in the list must be integers or floats")

def sort_large_list(items):
    validate_input(items)
    return sorted(items, reverse=True)

if __name__ == '__main__':
    sample_values = [5, 3, 8, 6, 2, 9, 1, 7, 4]
    print(sort_large_list(sample_values))