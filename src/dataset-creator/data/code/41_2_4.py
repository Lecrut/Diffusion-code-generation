def count_large_dataset(items):
    return sum(1 for _ in items)
if __name__ == '__main__':
    large_data = [i * i + 3 for i in range(0, 5_000_000)]
    result = count_large_dataset(large_data)
    print(result)