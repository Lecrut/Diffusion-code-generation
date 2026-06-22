def compute_mean():
    values = [10, 20, 30, 40, 50]
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    return total / count

if __name__ == '__main__':
    result = compute_mean()
    print(result)