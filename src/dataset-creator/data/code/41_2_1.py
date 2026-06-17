def count_items(data):
    return sum(1 for item in data)
if __name__ == '__main__':
    large_dataset = list(range(10_000_000))
    print(count_items(large_dataset))