def compute_mean(data):
    if not data:
        return None
    return sum(data) / len(data)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    mean_value = compute_mean(sample_data)
    print(mean_value)
    sample_data_2 = [1.5, 2.5, 3.5, 4.5]
    mean_value_2 = compute_mean(sample_data_2)
    print(mean_value_2)
    sample_data_3 = []
    mean_value_3 = compute_mean(sample_data_3)
    print(mean_value_3)