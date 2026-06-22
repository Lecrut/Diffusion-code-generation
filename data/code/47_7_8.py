def mean(values):
    if not values:
        return 0
    total = 0
    for v in values:
        total += v
    return total / len(values)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = mean(sample_list)
    print(result)