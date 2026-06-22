def find_mean(integers):
    if not integers:
        return 0.0
    total = 0
    count = 0
    for value in integers:
        total += value
        count += 1
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = find_mean(sample_data)
    print(result)