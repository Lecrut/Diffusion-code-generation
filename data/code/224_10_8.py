def compute_mean(data):
    if not data:
        return 0
    total = sum(data)
    count = len(data)
    return total / count

if __name__ == '__main__':
    values = [1.5, 2.5, 3.5]
    mean_value = compute_mean(values)
    print(f"Mean of {values}: {mean_value}")