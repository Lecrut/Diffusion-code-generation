def compute_mean(dataset):
    if not dataset:
        raise ValueError("Dataset cannot be empty")
    total_sum = sum(dataset)
    count = len(dataset)
    return total_sum / count

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = compute_mean(sample_data)
    print(result)