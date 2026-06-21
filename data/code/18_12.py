def get_median_index(values):
    n = len(values)
    if n == 0:
        raise ValueError("List cannot be empty")
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
    
    mid = n // 2
    if n % 2 == 1:
        return values[mid]
    else:
        return (values[mid - 1] + values[mid]) / 2

if __name__ == "__main__":
    sample_data = [7, 1, 3, 9, 5, 2, 8]
    result = get_median_index(sample_data)
    print(result)