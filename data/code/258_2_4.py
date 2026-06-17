def compute_means(data):
    if not data:
        return 0, 0
    sum1 = 0
    sum2 = 0
    count = len(data)
    for num1, num2 in data:
        sum1 += num1
        sum2 += num2
    mean1 = sum1 / count
    mean2 = sum2 / count
    return mean1, mean2
if __name__ == '__main__':
    sample_data = [(1, 5), (2, 8), (3, 10)]
    mean1, mean2 = compute_means(sample_data)
    print(f"Mean of first numbers: {mean1}")
    print(f"Mean of second numbers: {mean2}")
    empty_data = []
    mean1_empty, mean2_empty = compute_means(empty_data)
    print(f"Mean of first numbers for empty list: {mean1_empty}")
    print(f"Mean of second numbers for empty list: {mean2_empty}")
    sample_data_two = [(10, 20), (30, 40)]
    mean1_two, mean2_two = compute_means(sample_data_two)
    print(f"Mean of first numbers for second list: {mean1_two}")
    print(f"Mean of second numbers for second list: {mean2_two}")