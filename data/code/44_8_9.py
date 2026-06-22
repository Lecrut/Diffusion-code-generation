def compute_mean(values):
    if not values:
        return 0
    total = 0
    count = 0
    for value in values:
        total += value
        count += 1
    return total / count

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = compute_mean(sample_list)
    print(result)