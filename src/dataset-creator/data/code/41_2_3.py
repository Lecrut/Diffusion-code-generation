def count_items(data):
    return sum(1 for item in data) if isinstance(data, (list, tuple)) else len(list(item).__iter__())
if __name__ == '__main__':
    sample_data = [i * 2 for i in range(10_000_000)]
    print(count_items(sample_data))