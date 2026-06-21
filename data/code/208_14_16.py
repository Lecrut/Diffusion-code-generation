def mean_of_large_dataset(data):
    total = 0
    count = 0
    for value in data:
        total += value
        count += 1
    return total / count

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(mean_of_large_dataset(sample_data))