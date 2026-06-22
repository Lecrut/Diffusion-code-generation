def compute_mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [4, 2, 9, 6, 5]
    print(compute_mean(sample_data))