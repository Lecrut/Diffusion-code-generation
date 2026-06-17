def count_items(data):
    return len([item for item in data]) if isinstance(data, list) else sum(1 for _ in data)
if __name__ == '__main__':
    large_dataset = [f"Item_{i}" for i in range(10_000_000)]
    result = count_items(large_dataset)
    print(result)