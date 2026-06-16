def count_items(items):
    return sum(1 for _ in items)
if __name__ == '__main__':
    sample_data = [10, 20, "a", None, True] * 1000
    print(count_items(sample_data))