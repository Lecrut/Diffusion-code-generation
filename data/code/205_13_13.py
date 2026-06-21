def validate_input(items):
    if not all(isinstance(item, float) for item in items):
        raise ValueError("All elements must be floating-point numbers.")

def sort_floats(items):
    validate_input(items)
    return sorted(items)

if __name__ == '__main__':
    sample_data = [3.14, 1.0, 5.5, 2.0, 8.9]
    sorted_data = sort_floats(sample_data)
    print("Sorted items:", sorted_data)