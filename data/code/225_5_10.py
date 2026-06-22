import statistics

def compute_extremes(data: list) -> tuple:
    if not data:
        return None, None
    min_value = statistics.min(data)
    max_value = statistics.max(data)
    return min_value, max_value

if __name__ == '__main__':
    sample_data1 = [1, 5, 2, 8, 3]
    print(f"Sample Data 1: {sample_data1}, Min: {compute_extremes(sample_data1)}, Max: {compute_extremes(sample_data1)}")
    
    sample_data2 = [-10, 0, 5, -5]
    print(f"Sample Data 2: {sample_data2}, Min: {compute_extremes(sample_data2)}, Max: {compute_extremes(sample_data2)}")
    
    sample_data3 = [42]
    print(f"Sample Data 3: {sample_data3}, Min: {compute_extremes(sample_data3)}, Max: {compute_extremes(sample_data3)}")