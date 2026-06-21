def median_index(values):
    n = len(values)
    if n == 0:
        return None
    if n % 2 == 1:
        return values[n // 2]
    else:
        mid = n // 2
        return (values[mid - 1] + values[mid]) / 2

if __name__ == '__main__':
    sample_list = [7, 1, 3, 4, 6, 8, 2]
    result = median_index(sample_list)
    print(result)