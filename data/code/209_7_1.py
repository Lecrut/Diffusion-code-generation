def compute_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)
if __name__ == '__main__':
    large_list = list(range(10**6)) + [1, 2, 3]
    mean_value = compute_mean(large_list)
    print(mean_value)