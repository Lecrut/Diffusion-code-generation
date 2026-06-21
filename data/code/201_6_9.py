def compute_mean(data):
    if not data:
        raise ValueError("Data cannot be empty")
    total_sum = sum(data)
    count = len(data)
    return total_sum / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    try:
        mean = compute_mean(sample_data)
        print(f"Average: {mean}")
    except ValueError as e:
        print(e)