def count_items(data):
    return sum(1 for item in data) if isinstance(data, (list, tuple)) else len(list(item).__iter__())
if __name__ == '__main__':
    large_dataset = list(range(10_000_000))
    result = count_items(large_dataset)
    print(result)