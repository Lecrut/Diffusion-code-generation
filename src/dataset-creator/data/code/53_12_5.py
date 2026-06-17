def count_items_from_start(data):
    return sum(1 for item in data) if isinstance(data, (list, tuple)) else 0
if __name__ == '__main__':
    sample_data = [1, 'a', True, None] * 10**6
    print(count_items_from_start(sample_data))