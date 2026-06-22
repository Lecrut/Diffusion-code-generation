def compute_mean(values):
    if not values:
        raise ValueError("List cannot be empty")
    total = 0
    count = 0
    for number in values:
        total += number
        count += 1
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = compute_mean(sample_data)
    print(result)