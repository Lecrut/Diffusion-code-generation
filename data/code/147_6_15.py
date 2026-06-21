def sort_numeric_strings(numeric_strings):
    if not all(s.isdigit() for s in numeric_strings):
        raise ValueError("All elements must be numeric strings")
    
    return sorted(map(int, numeric_strings))

if __name__ == '__main__':
    sample_values = ["3", "1", "4", "1", "5", "9"]
    print(sort_numeric_strings(sample_values))