def compute_mean(data):
    if not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("All elements in the iterable must be numbers.")
    
    total = sum(data)
    count = len(data)
    
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    average = compute_mean(sample_data)
    print(f"Average: {average}")