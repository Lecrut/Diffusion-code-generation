def count_items(dataset):
    return sum(1 for _ in dataset)
if __name__ == '__main__':
    large_dataset = list(range(10_000_000))
    print(count_items(large_dataset))