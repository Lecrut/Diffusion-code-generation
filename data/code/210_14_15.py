def calculate_range(data):
    if not data:
        return 0
    return max(data) - min(data)

if __name__ == '__main__':
    sample_data_1 = [10, 5, 20, 3, 15]
    span_1 = calculate_range(sample_data_1)
    print(f"Data: {sample_data_1}, Range: {span_1}")
    
    sample_data_2 = [5.5, 1.2, 8.9, 3.0]
    span_2 = calculate_range(sample_data_2)
    print(f"\nData: {sample_data_2}, Range: {span_2}")
    
    sample_data_3 = []
    span_3 = calculate_range(sample_data_3)
    print(f"\nData: {sample_data_3}, Range: {span_3}")