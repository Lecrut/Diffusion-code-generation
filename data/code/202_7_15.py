def find_largest_in_range(start, end):
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    return end

if __name__ == '__main__':
    sample_values = {
        'range1': (5, 10),
        'range2': (-100, -50),
        'range3': (0, 0),
        'range4': (1, 100)
    }
    
    for name, values in sample_values.items():
        start, end = values
        print(f"Range {name}: ({start}, {end}), Largest: {find_largest_in_range(start, end)}")