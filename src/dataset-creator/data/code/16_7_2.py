def count_items(items):
    return sum(1 for _ in items)
if __name__ == '__main__':
    data = [10, 20, 30] + list(range(50)) * 100
    print(count_items(data))