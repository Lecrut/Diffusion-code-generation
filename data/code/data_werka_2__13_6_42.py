def validate_offsets(offsets):
    if not offsets:
        raise ValueError("The list of time zone offsets cannot be empty.")
    if not all(isinstance(offset, (int, float)) for offset in offsets):
        raise ValueError("All offsets must be integers or floats.")

def calculate_difference(offsets):
    validate_offsets(offsets)
    min_offset = find_minimum(offsets)
    max_offset = find_maximum(offsets)
    return max_offset - min_offset

def find_minimum(values):
    return min(values)

def find_maximum(values):
    return max(values)

if __name__ == '__main__':
    sample_offsets = [2, -5.5, 0, 4, -1]
    difference = calculate_difference(sample_offsets)
    print(difference)