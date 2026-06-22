def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2

def main():
    sample_values = [10, 5, 8, 12, 3]
    median_value = calculate_median(sample_values)
    print(median_value)

if __name__ == '__main__':
    main()