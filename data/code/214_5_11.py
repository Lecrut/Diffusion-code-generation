def filter_and_min(iterable):
    filtered_values = [value for value in iterable if value >= 0]
    return min(filtered_values) if filtered_values else None

if __name__ == '__main__':
    sample_data1 = [-3, -2, -1, 0, 1, 2, 3]
    print(f"Sample Data: {sample_data1}, Minimum Non-Negative: {filter_and_min(sample_data1)}")
    
    sample_data2 = [5, 4, 3, 2, 1]
    print(f"Sample Data: {sample_data2}, Minimum Non-Negative: {filter_and_min(sample_data2)}")
    
    sample_data3 = [-5, -4, -3, -2, -1]
    print(f"Sample Data: {sample_data3}, Minimum Non-Negative: {filter_and_min(sample_data3)}")