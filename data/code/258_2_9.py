def compute_means(data):
    if not data:
        return 0, 0
    sum1 = 0
    sum2 = 0
    count = len(data)
    for x, y in data:
        sum1 += x
        sum2 += y
    mean1 = sum1 / count
    mean2 = sum2 / count
    return mean1, mean2
if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6)]
    mean1, mean2 = compute_means(sample_data)
    print(f"Mean of first numbers: {mean1}")
    print(f"Mean of second numbers: {mean2}")
    empty_data = []
    mean1_empty, mean2_empty = compute_means(empty_data)
    print(f"Mean of first numbers (empty): {mean1_empty}")
    print(f"Mean of second numbers (empty): {mean2_empty}")
    sample_data_two = [(10, 20), (30, 40)]
    mean1_two, mean2_two = compute_means(sample_data_two)
    print(f"Mean of first numbers (two pairs): {mean1_two}")
    print(f"Mean of second numbers (two pairs): {mean2_two}")