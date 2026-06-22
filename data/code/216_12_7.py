def find_median(data):
    n = len(data)
    if n % 2 == 1:
        return sorted(data)[n // 2]
    else:
        return (sorted(data)[n // 2 - 1] + sorted(data)[n // 2]) / 2

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(find_median(sample_data))