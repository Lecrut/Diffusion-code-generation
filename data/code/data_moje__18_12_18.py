def get_median_index(values):
    n = len(values)
    if n == 0:
        return None
    if n % 2 == 1:
        return values[n // 2]
    lower = values[n // 2 - 1]
    upper = values[n // 2]
    return (lower + upper) / 2

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    result = get_median_index(sample_list)
    print(result)