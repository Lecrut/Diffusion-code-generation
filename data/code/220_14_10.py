def calculate_mean(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [3, 5, 7, 9]
    print(calculate_mean(sample_data))