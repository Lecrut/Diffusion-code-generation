def find_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    n = len(data)
    sorted_data = sorted(data)
    middle_index = n // 2
    
    if n % 2 == 1:
        return sorted_data[middle_index]
    else:
        lower_middle_index = middle_index - 1
        return (sorted_data[lower_middle_index] + sorted_data[middle_index]) / 2

if __name__ == '__main__':
    sample_list = [4, 7, 2, 5, 8]
    print(find_median(sample_list))