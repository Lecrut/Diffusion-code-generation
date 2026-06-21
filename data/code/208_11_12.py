def compute_mean(data):
    total = sum(data)
    count = len(data)
    if count == 0:
        return None
    return total / count

if __name__ == '__main__':
    sample_data = [15, 25.5, 35, 45.75]
    mean_value = compute_mean(sample_data)
    print(mean_value)