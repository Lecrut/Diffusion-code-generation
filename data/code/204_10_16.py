import statistics

def compute_median(data):
    if not data:
        raise ValueError("Data list cannot be empty")
    
    return statistics.median(data)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9]
    print(f"Median of {sample_data}: {compute_median(sample_data)}")