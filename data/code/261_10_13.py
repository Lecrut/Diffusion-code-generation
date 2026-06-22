def calculate_median(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    return sorted_data[n // 2] if n % 2 == 1 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

def main():
    sample_values = [5, 3, 8, 1, 4]
    print(calculate_median(sample_values))

if __name__ == '__main__':
    main()