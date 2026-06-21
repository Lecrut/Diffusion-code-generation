def compute_mean(data):
    if not data:
        raise ValueError("Data iterable cannot be empty")
    total = 0
    count = 0
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Item {item} is not a number")
        total += item
        count += 1
    return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(compute_mean(sample_data))