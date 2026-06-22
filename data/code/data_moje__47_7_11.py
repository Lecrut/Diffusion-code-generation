def compute_mean(data):
    if not data:
        raise ValueError("Data sequence must not be empty")
    total = 0
    count = 0
    for item in data:
        total += item
        count += 1
    return total / count

if __name__ == '__main__':
    values = [15, 25, 35, 45, 55]
    calculated_value = compute_mean(values)
    print(calculated_value)