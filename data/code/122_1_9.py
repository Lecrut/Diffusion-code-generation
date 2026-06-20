def average_large_dataset(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = (i for i in range(1000000))
    print(average_large_dataset(sample_data))