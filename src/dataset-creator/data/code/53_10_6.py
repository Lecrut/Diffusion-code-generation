def count_items(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    sample_data = [0, 1, 2, 3] + []
    result = count_items(sample_data)
    print(result)