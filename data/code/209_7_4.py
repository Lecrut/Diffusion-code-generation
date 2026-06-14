def compute_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)
if __name__ == '__main__':
    large_data = list(range(1000000))
    mean_value = compute_mean(large_data)
    print(mean_value)