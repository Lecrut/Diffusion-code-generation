def validate_input(items):
    if not all(isinstance(item, float) for item in items):
        raise ValueError("All elements in the tuple must be floating-point numbers")

def sort_tuple(items):
    return sorted(items)

if __name__ == '__main__':
    sample_data = (3.14, 1.0, 5.5, 2.0, 8.9)
    validate_input(sample_data)
    result = sort_tuple(sample_data)
    print("Sorted tuple:", result)