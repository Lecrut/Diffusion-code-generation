def sum_large_dataset(data_generator):
    total = 0
    for item in data_generator:
        if not isinstance(item, (int, float)):
            raise ValueError("Invalid data type in dataset")
        total += item
    return total

if __name__ == '__main__':
    sample_data = [1.5, 2, 3, 4.5, 5]
    result = sum_large_dataset(iter(sample_data))
    print(f"Sum of the dataset: {result}")