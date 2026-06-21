def compute_average(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Input must be a non-empty list of floats")
    
    total_sum = sum(data)
    count = len(data)
    mean_value = total_sum / count
    
    return mean_value

if __name__ == '__main__':
    sample_data = [1.8, 2.2, 3.0, 4.6]
    average = compute_average(sample_data)
    print(average)