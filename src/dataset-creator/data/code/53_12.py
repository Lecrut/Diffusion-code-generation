def count_items_from_start(data):
    return sum(1 for _ in data)
if __name__ == '__main__':
    sample_data = list(range(0, 1_000_000))
    result = count_items_from_start(sample_data)
    print(result)