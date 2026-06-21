def min_item(items):
    return min((item for item in items), default=None)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(min_item(sample_values))