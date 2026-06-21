import statistics

def calculate_range(data):
    if not isinstance(data, list) or not data:
        raise ValueError("Input must be a non-empty list of numbers.")
    
    return max(data) - min(data)

if __name__ == '__main__':
    sample_dataset1 = [10, 5, 20, 15]
    sample_dataset2 = [3, 8, 1, 9, 4]
    print(calculate_range(sample_dataset1))
    print(calculate_range(sample_dataset2))