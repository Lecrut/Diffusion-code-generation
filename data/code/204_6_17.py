def find_median(data):
    if len(data) != 3:
        raise ValueError("Input list must contain exactly three integers")
    
    sorted_data = sorted(data)
    return sorted_data[1]

if __name__ == '__main__':
    sample_list = [5, 2, 8]
    print(f"Median of {sample_list}: {find_median(sample_list)}")