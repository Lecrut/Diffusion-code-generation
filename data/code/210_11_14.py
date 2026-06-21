DATA_SAMPLE_1 = [1, 5, 2, 8, 3]
DATA_SAMPLE_2 = [10, 20, 5, 15]
EMPTY_DATA_LIST = []

def calculate_data_range(data):
    if not data:
        raise ValueError("Input list cannot be empty.")
    return max(data) - min(data)

if __name__ == '__main__':
    try:
        range1 = calculate_data_range(DATA_SAMPLE_1)
        print(f"Data Range for {DATA_SAMPLE_1}: {range1}")
        
        range2 = calculate_data_range(DATA_SAMPLE_2)
        print(f"Data Range for {DATA_SAMPLE_2}: {range2}")
        
        calculate_data_range(EMPTY_DATA_LIST)
    except ValueError as e:
        print(f"Error caught: {e}")