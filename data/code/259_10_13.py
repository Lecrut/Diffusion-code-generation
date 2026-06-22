def find_extremes(data):
    if not data:
        return None

    def validate_data():
        nonlocal data
        if not all(isinstance(x, int) for x in data):
            raise ValueError("All elements must be integers")

    validate_data()
    
    smallest = min(data)
    largest = max(data)
    return smallest, largest

if __name__ == '__main__':
    sample_list = [34, 12, 56, 89, 4, 72, 23]
    result = find_extremes(sample_list)
    print(f"Smallest value: {result[0]}")
    print(f"Largest value: {result[1]}")