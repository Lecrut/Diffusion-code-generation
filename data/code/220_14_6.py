def compute_mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(compute_mean(sample_data))