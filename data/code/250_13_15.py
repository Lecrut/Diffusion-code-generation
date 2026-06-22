def validate_data(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    for value in data:
        if not isinstance(value, (int, float)):
            raise TypeError("All elements must be integers or floats")

def compute_mean(data):
    validate_data(data)
    return sum(data) / len(data)

if __name__ == '__main__':
    sample1 = [10.5, 20.5, 30.5]
    print(f"Data: {sample1}, Mean: {compute_mean(sample1)}")
    
    sample2 = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(f"Data: {sample2}, Mean: {compute_mean(sample2)}")
    
    sample3 = [100.0, 50.5, 75.25]
    print(f"Data: {sample3}, Mean: {compute_mean(sample3)}")
    
    sample4 = [3.14, 2.71, 1.618]
    print(f"Data: {sample4}, Mean: {compute_mean(sample4)}")