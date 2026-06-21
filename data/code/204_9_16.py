def find_median(values):
    values.sort()
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2.0
    else:
        return values[mid]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_median(sample_values))