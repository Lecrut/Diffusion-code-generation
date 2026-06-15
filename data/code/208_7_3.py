def compute_mean(data):
    if not data:
        return None
    return sum(data) / len(data)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    mean_value = compute_mean(sample_data)
    print(mean_value)